n, m = map(int,input().split())
p = [[i] + list(map(int,input().split())) for i in range(m)]
p = sorted(p, key=lambda x:(x[1], x[2]))
for i in range(m):
    p[i][1] = str(p[i][1]).zfill(6)
    if i >= 1 and p[i][1] == p[i-1][1]:
        p[i][2] = str(int(p[i-1][2])+1).zfill(6)
    else:
        p[i][2] = str(1).zfill(6)
p = sorted(p, key=lambda x:(x[0]))
for i in range(m):
    print(p[i][1]+p[i][2])