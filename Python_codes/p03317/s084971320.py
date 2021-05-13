N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1 + (N - K) // (K - 1)
if (N - K) % (K - 1) != 0:
    ans += 1
print(ans)