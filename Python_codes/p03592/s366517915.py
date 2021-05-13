n, m, k = [int(i) for i in input().split()]
grid = [0]

# O(nm)

for i in range(n + 1):
    for j in range(m + 1):
        black = (i * m) + (n - 2 * i) * j
        if black == k:
            print("Yes")
            quit()
print("No")
