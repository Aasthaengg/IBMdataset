## coding: UTF-8
#累積和
N = int(input())
U = list(map(int,input().split()))
D = list(map(int,input().split()))

U = U[::-1]
D = D[::-1]

up = 0
down = 0
upper = [0]
downer = []
for i in range(N):
    up += U[i]
    down += D[i]
    upper.append(up)
    downer.append(down)
upper = upper[::-1]
downer = downer[::-1]
#print(upper)
#print(downer)

ans = 0
for i in range(N):
    ret = upper[0] - upper[i+1] + downer[i]
    ans = max(ans, ret)
print(ans)