n = int(input())
x = []
med = []
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    x.append((ai, bi))
    a.append(ai)
    b.append(bi)
a.sort()
b.sort()

if n % 2 == 1:
    min_med = a[(n+1)//2 - 1]
    max_med = b[(n+1)//2 - 1]
    print(max_med - min_med + 1)
else:
    min_med = (a[n//2 - 1] + a[n//2]) / 2
    max_med = (b[n//2 - 1] + b[n//2]) / 2
    ans = (max_med - min_med) / 0.5
    ans += 1
    ans = int(ans)
    print(ans)
