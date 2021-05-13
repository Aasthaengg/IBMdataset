n,t = map(int,input().split())
A = list(map(int,input().split()))
inf = float('inf')
m = [0]*n
m[0] = A[0]
M = [0]*n
M[n-1] = A[n-1]
for i in range(n-1):
    m[i+1] = min(m[i],A[i+1])
    M[n-i-2] = max(M[n-i-1],A[n-2-i])

delta = [M[i+1] - m[i] for i in range(n-1)]
can = max(delta)
ans = 0
for i,a in enumerate(A):
    if a == m[i] + can:
        ans += 1
print(ans)
