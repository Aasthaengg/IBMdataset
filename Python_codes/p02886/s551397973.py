n = int(input())
d = [int(s) for s in input().split()]

total = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        total += d[i] * d[j]
print(total)
