n, m = map(int, input().split())
XYZ = []
JKL = []
Seihu = [-1, 1]
for i in range(n):
    x, y, z = map(int, input().split())
    XYZ.append([x,y,z])
    for j in Seihu:
        for k in Seihu:
            for l in Seihu:
                tot = x*j + y*k + z*l
                XYZ[i].append(tot)
for j in Seihu:
    for k in Seihu:
        for l in Seihu:
            JKL.append([j,k,l])

ans = 0
for i in range(8):
    jkl = JKL[i]
    XYZ = sorted(XYZ, key=lambda x:x[i+3], reverse=True)
    score = 0
    for x in range(m):
        score += XYZ[x][i+3]
    ans = max(ans, score)

print(ans)