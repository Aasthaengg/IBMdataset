n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
    n = n - a[i]
print(int(n) if n >= 0 else "-1")