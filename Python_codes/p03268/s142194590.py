N, K = map(int, input().split())

ans = 0
for a in range(1, N+1):
    if(2 * a % K == 0):
        beg = K - a % K
        end = N
        cnt = (end - beg + K) // K
        ans += cnt * cnt

print(ans)