n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
y = sorted(x)
z = sorted(x, key=lambda x: x[1])

if n % 2 == 1:
    print(z[n//2][1] - y[n//2][0] + 1)
else:
    a = y[n//2-1][0]
    b = y[n//2][0]
    c = z[n//2-1][1]
    d = z[n//2][1]
    e = (c + d) / 2
    f = (a + b) / 2
    print(int((e - f) * 2) + 1)