n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))

tmp1 = []
tmp2 = []
for i in range(n):
    tmp1.append([xy[i][0]+xy[i][1], xy[i][0], xy[i][1]])
    tmp2.append([xy[i][0]-xy[i][1], xy[i][0], xy[i][1]])
tmp1.sort()
tmp2.sort()

if n <= 10:
    ii = n
    jj = n+1
else:
    ii = 10
    jj = 10

ans = 0
for i in range(ii):
    for j in range(1, jj):
        if (tmp1[-j][2]-tmp1[i][2])*(tmp1[-j][1]-tmp1[i][1]) >= 0:
            tmp = tmp1[-j][0]-tmp1[i][0]
            ans = max(tmp, ans)
        if (tmp2[-j][2]-tmp2[i][2])*(tmp2[-j][1]-tmp2[i][1]) <= 0:
            tmp = tmp2[-j][0]-tmp2[i][0]
            ans = max(tmp, ans)

print(ans)