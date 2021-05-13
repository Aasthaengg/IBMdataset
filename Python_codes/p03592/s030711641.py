n, m, k = map(int, input().split())

if k == 0 or k == n * m:
    print("Yes")
    exit()

for i in range(n + 1):
    for j in range(m + 1):
        if i * j + (n - i) * (m - j) == k:
            print("Yes")
            exit()
print("No")