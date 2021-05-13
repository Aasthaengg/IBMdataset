N, K = map(int, input().split())

tmp = N // K

ans = N - K * tmp

ans = min(ans, abs(ans - K))

print(ans)
