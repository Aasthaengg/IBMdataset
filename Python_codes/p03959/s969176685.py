N = int(input())
T = [0]+list(map(int,input().split()))+[float('inf')]
A = [float('inf')]+list(map(int,input().split()))+[0]
ans = 1
MOD = 10**9+7
for i in range(1,N+1):
    if T[i-1] < T[i]:
        ans *= int(T[i] <= A[i])
    if A[i] > A[i+1]:
        ans *= int(T[i] >= A[i])
    if T[i-1] == T[i] and A[i+1] == A[i]:
        ans *= min(T[i],A[i])
        ans %= MOD
print(ans)