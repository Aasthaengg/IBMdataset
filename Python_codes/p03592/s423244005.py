n, m, k = map(int, input().split())

for row in range(n+1):
    for col in range(m+1):
        if row * m + col * n - 2 * (row * col) == k:
            print('Yes')
            exit()

print('No')
