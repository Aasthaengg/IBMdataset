N,D,A = map(int,input().split())
data = [list(map(int,input().split())) for i in range(N)]

from math import ceil

B = []
for i in range(N):
    B.append((data[i][0],ceil(data[i][1]/A)))

B = [(0,0)] + sorted(B)

C = [0]  #C[i] = (X[j] <= X[i]+2*D たる最大の j)
for i in range(1,N+1):
    a = i
    b = N+1
    while a+1 < b:
        mid = (a+b)//2
        if B[mid][0] <= B[i][0] + 2*D:
            a = mid
        else:
            b = mid
    C.append(a)

D = [0]*(N+2)  #D[i] = (i番目の敵が攻撃される回数)
ans = 0
for i in range(1,N+1):
    D[i] = max(0,D[i-1]+D[i])
    if D[i] >= B[i][1]:
        continue
    else:
        k = -D[i]+B[i][1]
        D[i] += k
        D[C[i]+1] -= k
        ans += k
print(ans)