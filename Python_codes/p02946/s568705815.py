K, X = [int(i) for i in input().split()]
list = [int(X - (K-1) + i) for i in range((K - 1) * 2 + 1)]

print(*list)