import math

n, d, a = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()
q = []
index = 0
ans = 0
dmg = 0
for i in range(n):
    while index < len(q) and q[index][0] < l[i][0]:
        dmg -= q[index][1]
        index += 1
    if l[i][1] > dmg:
        times = (l[i][1]-dmg)//a if (l[i][1]-dmg)%a == 0 else (l[i][1]-dmg)//a+1
        ans += times
        q.append((l[i][0]+2*d, a*times))
        dmg += a*times
print(ans)