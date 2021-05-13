n, a, b = map(int, input().split())
x = list(map(int, input().split()))
now = x[0]
sc = 0
for i in range(1, n):
    if abs(now - x[i])*a < b:
        sc += abs(now - x[i])*a
    else:
        sc += b
    now = x[i]
print(sc)