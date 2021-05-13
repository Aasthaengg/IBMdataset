N=int(input())
*T, = [0] + list(map(int,input().split())) + [0]
*A, = [0] + list(map(int,input().split())) + [0]
mod = 10**9+7
M = list(map(min,zip(A,T)))[1:-1]
m = [max(T[i] if T[i]>T[i-1] else 1, A[i] if A[i]>A[i+1] else 1) for i in range(1,N+1)]
ans = 1
for a,b in zip(m,M): ans = ans * max(0,b-a+1) % mod
print(ans)