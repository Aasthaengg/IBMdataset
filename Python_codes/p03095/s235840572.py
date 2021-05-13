from collections import defaultdict
mod = 10**9+7
n = int(input())
s = list(input())
ans = 1
dd = defaultdict(lambda:0)
for i in s:
    dd[i] += 1
for key in dd:
    ans *= dd[key]+1
    ans %= mod
ans -= 1
print(ans)