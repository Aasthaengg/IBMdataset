import sys
from collections import defaultdict
from copy import deepcopy
import itertools
input = sys.stdin.readline
# 文字列の場合は普通のinput()を使うか下を使う
# input = sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0] + list(itertools.accumulate(A))
"""
「iからjまで」--->「0からjまで」-「0から(i - 1)まで」
に分解すれば、求める条件は
(S[j] - S[i]) % K = j - i
と書ける。これを式変形して
S[j] - j = S[i] - i mod K "with j - i < K"
とすれば、次を示せばよい：

For 1 <= j <= N, count the number of j - K < i < j
such that S[j] - j = S[i] - i mod K
"""

if K == 1:
    print(0)
    exit()

d = defaultdict(int)
d[(S[0] - 0) % K] = 1

ans = 0
for j in range(1, N + 1):
    x = (S[j] - j) % K
    ans += d[x]
    d[x] += 1
    if j - K >= -1:
        y = (S[j - K + 1] - (j - K + 1)) % K
        d[y] -= 1

print(ans)