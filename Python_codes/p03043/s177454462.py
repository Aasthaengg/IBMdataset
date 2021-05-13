n, k = list(map(int, input().split()))

p = 0

for i in range(1, n+1):
    j = i
    q = 1 / n
    while j < k:
        q *= 1 / 2
        j *= 2
    p += q

print(p)