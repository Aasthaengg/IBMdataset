n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
l = []
ans = -1000
for i in range(n):
    if s[i] not in l:
        l.append(s[i])
        pnt = s.count(s[i]) - t.count(s[i])
        ans = max(ans, pnt)
if ans < 0:
    print(0)
else:
    print(ans)
