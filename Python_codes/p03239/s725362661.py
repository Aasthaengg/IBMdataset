n,t = map(int,input().split())
c = [list(map(int,input().split())) for i in range(n)]
p = []

for i in range(n):
    if c[i][1] <= t:
        p.append(c[i][0])

if len(p) == 0:
    print('TLE')
else:
    p.sort()
    print(p[0])