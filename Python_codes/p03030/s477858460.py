n = int(input())
xs = [0] * n
for i in range(n):
    s, p = input().split()
    xs[i] = [s, int(p), i + 1]
xs.sort(key=lambda v: (v[0], 100 - v[1]))
print(*map(lambda v: v[2], xs), sep="\n")
