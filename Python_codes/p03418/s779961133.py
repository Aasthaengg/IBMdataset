N , K = map(int , input().split())
ans = 0
if K == 0:
    print(N * N)
    exit(0)
for b in range(1, N + 1):
    ans += int(N / b) * max(0,b - K) + max(N % b - K + 1 ,0)
print(ans)