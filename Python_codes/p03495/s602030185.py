from collections import Counter
import sys

N, K = map(int, input().split())
A = list(input().split())
ball = [int(A[i]) for i in range(N)]
kinds = len(set(ball))
Cou = list(Counter(ball).most_common())
dele = [int(Cou[i][1]) for i in range(len(Cou) - kinds + K, len(Cou))]
print(sum(dele))
