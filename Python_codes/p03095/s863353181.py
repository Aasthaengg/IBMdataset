from collections import Counter
n = int(input())
s = input()
mod = 1000000007
ans = 1
cnt = Counter(s)
for v in cnt.values(): ans = ans*(v+1)%mod
ans = (ans-1)%mod
print(ans)