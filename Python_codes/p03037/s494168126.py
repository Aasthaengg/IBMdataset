n, m = map(int, input().split())
a = 0; b = n+1
for _ in range(m):
    l, r = map(int, input().split())
    a = max(a, l)
    b = min(b, r)
print(max(0, b-a+1))