d, n = map(int, input().split())
print([i*100**d for i in range(1, 102) if i != 100][n - 1])