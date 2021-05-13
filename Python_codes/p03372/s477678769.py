N,C = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
V = [0 for _ in range(N)]
Vm = [0 for _ in range(N)]
V[0] = A[0][1]-A[0][0]
Vm[0] = V[0]
for i in range(1,N):
    V[i] = V[i-1]+A[i][1]-(A[i][0]-A[i-1][0])
    Vm[i] = max(V[i],Vm[i-1])
U = [0 for _ in range(N)]
Um = [0 for _ in range(N)]
U[0] = A[-1][1]-(C-A[-1][0])
Um[0] = U[0]
for j in range(2,N+1):
    U[j-1] = U[j-2]+A[-j][1]-(A[-(j-1)][0]-A[-j][0])
    Um[j-1] = max(U[j-1],Um[j-2])
ans = V[N-1]
for i in range(N-1):
    ans = max(ans,V[i],V[i]-A[i][0]+Um[N-2-i])
ans = max(ans,U[N-1])
for j in range(N-1):
    ans = max(ans,U[j],U[j]-(C-A[-(j+1)][0])+Vm[N-2-j])
print(max(ans,0))