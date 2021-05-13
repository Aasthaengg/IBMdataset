import math
N = int(input())

s1 = []
s2 = []
#visited
for i in range(N):
    x, y = map(int, input().split())
    d0 = x + y
    d1 = x - y
    #if d0 in s1 and d1 in s2 and s1.index(d0) == s2.index(d1):
    #    continue
    s1.append(d0)
    s2.append(d1)


ans = 0

if len(s1) > 1 and len(s2) > 1:
    s1s = sorted(s1)
    s2s = sorted(s2)

    ans = max(s1s[0] - s1s[-1], s2s[0] - s2s[-1]
              , s1s[-1] - s1s[0], s2s[-1] - s2s[0])

print(int(ans))


