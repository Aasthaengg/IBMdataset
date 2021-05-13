N,x = list(map(int,input().split()))
A = list(map(int,input().split()))

ans=0

n=0
if A[n] > x:
    ans += A[n]-x
    A[n] = x

for n in range(1,N):
    if A[n-1]+A[n] > x:
        ans += A[n]-(x-A[n-1])
        A[n] = x-A[n-1]
        
print(ans)