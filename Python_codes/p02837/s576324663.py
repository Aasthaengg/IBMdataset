import itertools
N=int(input())
A=[]
Z=[]
for _ in range(N):
    a_i=int(input())
    z_i=[]
    A.append(a_i)
    for i in range(a_i):
        a,b=map(int,input().split())
        z_i.append([a-1,b])
    Z.append(z_i)
ans=0
for bit in itertools.product([0,1],repeat=N):
    f=True
    for j in range(N):
        if bit[j]==1:
            for k in range(A[j]):
                if bit[Z[j][k][0]]!=Z[j][k][1]:
                    f=False
                    break
    if f:
        ans=max(ans,bit.count(1))
print(ans)