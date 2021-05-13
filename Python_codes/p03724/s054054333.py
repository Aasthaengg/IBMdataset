N,M = map(int,input().split())
C = {i:0 for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    C[a] = (C[a]+1)%2
    C[b] = (C[b]+1)%2
flag = 0
for i in range(1,N+1):
    if C[i]==1:
        flag = 1
        break
if flag==0:
    print("YES")
else:
    print("NO")