N=int(input())

A=[0]*N
B=[0]*N
for i in range(N):
    a,b=map(int, input().split())
    A[i]=a
    B[i]=b
count=0
#print(A,B)
for i in range(N-1,-1,-1):
    X=(A[i]+count)%B[i]
    if X!=0:
        res=B[i]-(A[i]+count)%B[i]
        count+=res

print(count)