n, m, k = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(1,n):
    A[i] += A[i-1]
for i in range(1,m):
    B[i] += B[i-1]
A.insert(0,0)
B.insert(0,0)

j = m
ans = 0
for i in range(n+1):
    if A[i] > k:
        break
    
    while B[j] > k-A[i]:
        j -= 1
    ans = max(ans, i+j)

print(ans)
