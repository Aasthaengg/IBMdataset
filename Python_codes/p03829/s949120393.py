n, a, b = map(int, input().split())
xs = list(map(int, input().split()))
res = 0
for i in range(n-1):
    walk = (xs[i+1]-xs[i])*a
    if walk <= b:
        res += walk
    else:
        res += b
print(res)