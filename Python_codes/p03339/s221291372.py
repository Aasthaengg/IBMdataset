N=int(input())
A=list(input())

E_l=[0]*N
for n in range(1,N):
    E_l[n]=E_l[n-1]
    if A[n-1] == 'W':
        E_l[n]+=1
    
W_r=[0]*N
for n in range(N-2,-1,-1):
    W_r[n] = W_r[n+1]
    if A[n+1] == 'E':
        W_r[n]+=1

ans=10**20
for n in range(N):
    if ans > E_l[n]+W_r[n]:
        ans=E_l[n]+W_r[n]
print(ans)