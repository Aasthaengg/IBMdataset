n, k = map(int, input().split())
m = (n - 1) * (n - 2) // 2
if k > m:
    print(-1)
    exit(0)
print(n + m - k - 1)
for i in range(1, n):
    print(i, n)
for i in range(1, n):
    for j in range(i + 1, n):
        if m == k:
            exit(0)
        print(i, j)
        k += 1