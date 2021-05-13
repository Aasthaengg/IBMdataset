n, m, k = list(map(int, input().split()))

flag = False
for y in range(m+1):
    for x in range(n + 1):
        if n * y + m * x - 2 * x * y == k:
            flag = True
            break
print("Yes" if flag else "No")