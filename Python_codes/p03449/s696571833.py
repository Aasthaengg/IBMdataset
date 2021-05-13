n = int(input())
A1 = tuple(map(int, input().split()))
A2 = tuple(map(int, input().split()))

from itertools import accumulate
A1S = [0] + list(accumulate(A1))
A2S = [0] + list(accumulate(A2))

ma = 0
for i in range(1, n+1):
    ma = max(ma, A1S[i] + A2S[-1] - A2S[i-1])
print(ma)