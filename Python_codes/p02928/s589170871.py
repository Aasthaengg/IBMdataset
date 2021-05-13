n, k = map(int, input().split())
a = list(map(int, input().split()))
total_1 = 0
for i in range (n - 1):
    for j in range (i + 1, n):
        if a[i] > a[j]:
            total_1 += 1
total_2 = 0
for i in range (n):
    for j in range (n):
        if a[i] > a[j]:
            total_2 += 1
print((total_1 * k + (total_2 * k * (k - 1)) // 2) % (10 ** 9 + 7))