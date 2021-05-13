K = int(input())


N = 50
cnt = [K // 50 + (1 if K % 50 > i else 0) for i in range(50)]
A = [49 + (50 * c) - (K - c) for c in cnt]
print(N)
print(*A, sep=' ')
