n,k=map(int,input().split())
if (n-2)*(n-1) < k*2:
    print(-1)
    exit()

a=(n-2)*(n-1)//2
print(n-1-k+a)
for i in range(1,n):
    print(1,i+1)

A=[]
for i in range(1,n):
    for j in range(1,i):
        A.append([i+1,j+1])
        
for i in range(a-k):
    print(*A[i])
