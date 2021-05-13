N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=[0]*(N-1)
a=A[0]
z=A[-1]

for i in range(1,N-1):
    if A[i]>=0:
        ans[i-1]=(a,A[i])
        a-=A[i]
    else:
        ans[i-1]=(z,A[i])
        z-=A[i]
ans[N-2]=(z,a)
print(z-a)
for s in ans:
    print(*s)