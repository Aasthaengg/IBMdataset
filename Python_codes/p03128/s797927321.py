import math
from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))

if 9 in a and 6 in a:
    a.remove(6)
if 5 in a:
    if 2 in a:
        a.remove(2)
    if 3 in a:
        a.remove(3)
if 3 in a and 2 in a:
    a.remove(2)

req_m = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [None] * (n+1)
dp[0] = Counter([])

int_dp = [0] * (n+1)

for i in range(1, n+1):
    for j in a:
        if i >= req_m[j] and dp[i-req_m[j]] is not None:
            v = dp[i-req_m[j]] + Counter([j])
            if dp[i] is None:
                dp[i] = v
            else:
                if sum(dp[i].values()) < sum(v.values()):
                    dp[i] = v
                elif sum(dp[i].values()) == sum(v.values()):
                    if sorted(dp[i].elements(), reverse=True) < sorted(v.elements(), reverse=True):
                        dp[i] = v

print(''.join(map(str, sorted(dp[-1].elements(), reverse=True))))
