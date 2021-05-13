K, X = map(int, input().split())

min_X = X - K + 1
max_X = X + K - 1

ans = [i for i in range(min_X, max_X+1)]
print(*ans)
