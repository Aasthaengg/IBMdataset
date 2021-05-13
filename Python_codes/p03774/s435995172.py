# coding = SJIS

n, m = map(int, input().split())
ab = []
for i in range(n):
    an, bn = map(int, input().split())
    ab.append([an, bn])
cd = []
for i in range(m):
    cn, dn = map(int, input().split())
    cd.append([cn, dn])

for i in range(n):
    dis = []
    for j in range(m):
        dis.append(abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]))
    print((dis.index(min(dis)) + 1))