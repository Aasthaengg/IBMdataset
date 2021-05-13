n, m, k = map(int, input().split())

val = []

for i in range(0, n + 1):
    for j in range(1, m + 1):
        x = i * j + (n - i) * (m - j)
        val.append(x)
        
val = set(val)

print("Yes" if k in val else "No")