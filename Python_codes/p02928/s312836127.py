n,k=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        if A[i]>A[j]:
            cnt+=1
Aij=A+A
l=len(Aij)
cntij=0
for i in range(l-1):
    for j in range(i+1,l):
        if Aij[i]>Aij[j]:
            cntij+=1
cntij-=2*cnt
Tii=cnt*k
Tij=cntij*(k*(k-1)//2)
print((Tii+Tij)%mod)
