K, X = map(int, input().split())

min_x = max(X-(K-1), -1000000)
max_x = min(X+(K-1), 1000000)

ans = list(range(min_x, max_x+1))

print(*ans)
