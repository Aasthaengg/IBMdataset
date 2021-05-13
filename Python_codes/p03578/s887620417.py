n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
import collections
cd = collections.Counter(t)
ct = collections.Counter(d)

ans = 1
for i in range(m):
    if ct[t[i]] < cd[t[i]]:
        ans = 0
if ans == 0:
    print("NO")
else:
    print("YES")