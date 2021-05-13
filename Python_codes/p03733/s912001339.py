N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
rest_time = T
tmp = 0
for i in range(1, N):
    ans += min(T, A[i]-A[i-1])

ans += T
print(ans)
