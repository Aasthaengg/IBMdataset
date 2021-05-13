n, m, x = map(int, input().split())
a = list(map(int, input().split()))

b = sum(1 for i in range(m) if a[i] <= x)

print(min(b, m - b))
