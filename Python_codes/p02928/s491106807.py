n,k = map(int,input().split())
A = list(map(int,input().split()))

k1 = ((k-1)*k//2)
k2= ((k)*(k+1)//2)

normal = 0
reverse = 0
for i in range(n):
    normal += sum(1 for a in A[i+1:] if a > A[i])
    reverse += sum(1 for a in A[i+1:] if a < A[i])

print((normal * k1 + reverse * k2)%(10**9 + 7))