import itertools

n=int(input())
f=[[]]*n
for i in range(n):
    fij=list(map(int,input().split()))
#    f[i].append(fij)
    f[i]=fij
p=[[]]*n
for i in range(n):
    pij=list(map(int,input().split()))
    p[i]=pij
    
pmax=-10**11
for a in itertools.product([0,1], repeat=10):
    if sum(a)==0:
        continue
    psum=0
    for ni in range(n):
        k=0
        for i in range(10):
            if f[ni][i]==1 and a[i]==1:
                k+=1
        psum=psum+p[ni][k] 
    pmax=max(pmax,psum)   

print(pmax)
