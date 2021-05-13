r, g, b, n = map(int, input().split())
count = 0
for i in range(0, n + 1, r):
    for j in range(0, n + 1, g):
        if i + j > n:
            break
        k = n - i - j
        if k % b == 0:
            count += 1

print(count)