n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort(reverse=True)
xmax = max(x[0], X)
y.sort()
ymin = min(y[0], Y)

if ymin - xmax > 0:
    print("No War")
else:
    print("War")
