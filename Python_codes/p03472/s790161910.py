from math import ceil
N,H=map(int, input().split())

A=[0]*N
B=[0]*N
for i in range(N):
    a,b=map(int, input().split())
    A[i]=a
    B[i]=b

A=sorted(A)
B=sorted(B, reverse=True)
amax=max(A)

ans=0

for i in range(N):
    b=B[i]
    if b>amax:
        H-=b
        ans+=1
        if H<=0:
            break
    else:
        break
if H>0:
    ans+=ceil(H/amax)
print(ans)
