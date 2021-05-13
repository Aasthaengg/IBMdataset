N=int(input())
A=[0]*N
B=[0]*N

for i in range(N):
    a,b=map(int,input().split())
    A[i]=a
    B[i]=b

A=A[::-1]
B=B[::-1]

K=0
for i in range(N):
    if (A[i]+K)%B[i]:
        L=B[i]-((A[i]+K)%B[i])
        K+=L
print(K)
