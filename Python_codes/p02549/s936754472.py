n,k=map(int,input().split())
L=[]
R=[]
h=[0,1,-1]+[0]*400010
M=998244353
for i in range (k):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
N=0
for i in range (1,n):
    N=(N+h[i]+100*M)%M
    for j in range (k):
        h[L[j]+i]+=N
        h[R[j]+i+1]-=N
print(((N+h[n])+100*M)%M)