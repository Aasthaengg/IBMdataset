N, K = map(int, input().split())

for i in range(1, N+1):
    if i%2 != 0:
        K -= 1

print('YES' if K <= 0 else 'NO')