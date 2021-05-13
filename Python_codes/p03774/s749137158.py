n, m = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

cd = []
for i in range(m):
    cd.append(list(map(int, input().split())))
# print(ab)
# print(cd)

for i in range(n):
    r = 999999999999999999
    cp = -1
    for j in range(m):
        if abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]) < r:
            r = abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
            cp = j
    print(cp+1)
