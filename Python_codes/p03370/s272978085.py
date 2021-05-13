n, x = map(int, input().split())
m = sorted(map(int, [input() for i in range(n)]))

x = x - sum(m)
print(n + x // m[0])
