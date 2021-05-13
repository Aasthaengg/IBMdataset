N = int(input())
A=[]
xy=[]
for i in range(N):
    a=int(input())
    A.append(a)
    X = [list(map(int, input().split())) for i in range(a)]
    xy.append(X)
mx=0

for i in range(2**N):
    Z=[0]*N
    flag=0
    for j in range(N):
        if ((i>>j)&1):
            Z[j]=1
    for k in range(N):
        for l in range(A[k]):
            if Z[k]==1:
                if Z[xy[k][l][0]-1]!=xy[k][l][1]:
                    flag=1
    if flag==0:
        mx=max(mx,Z.count(1))
print(mx)

