from operator import itemgetter

N = int(input())
XL = [list(map(int,input().split())) for i in range(N)]
a = []
b = []

for i in range(N):
    a_temp = XL[i][0] - XL[i][1]
    b_temp = XL[i][0] + XL[i][1]
    a.append(a_temp)
    b.append(b_temp)

XL = sorted([(a[i], b[i]) for i in range(N)], key=itemgetter(1))

ans = 1
last = XL[0][1]

for i in range(N):
    if last <= XL[i][0] :
        last = XL[i][1]
        ans += 1

print(ans)