n, m, k = [int(w) for w in input().split()]

cond = False

for i in range(n + 1):
    for j in range(m + 1):
        b = i * (m - j) + j * (n - i)
        if b == k:
            cond = True
            break
    if cond:
        break

print("Yes" if cond else "No")
