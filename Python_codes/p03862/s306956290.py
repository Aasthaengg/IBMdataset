N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    d = max(0, (A[i] + A[i+1]) - x)
    
    ans += d
    if A[i+1] >= d:
        A[i+1] -= d
    else:
        d -= A[i+1]
        A[i+1] = 0
        A[i] -= d
    
print(ans)
