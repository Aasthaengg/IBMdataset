n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(m)]
d = {}
for i in range(n):
    for j in range(m):
        d[j] = abs(s[i][0]-c[j][0])+abs(s[i][1]-c[j][1])
    t = sorted(d.items(), key=lambda x:x[1])
    print(t[0][0]+1)
    d = {}