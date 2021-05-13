N=int(input())
T=list(map(int,input().split()))
M=int(input())
total=0
for i in range(N):
    total+=T[i]
for i in range(M):
    K=total
    P,X=map(int,input().split())
    K=K-T[P-1]
    K+=X
    print(K)