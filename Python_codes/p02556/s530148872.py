n = int(input())
xx = []
yy = []
for _ in range(n):
    x, y = map(int, input().split())
    xx.append(x + y)
    yy.append(x - y)

print(max(max(xx) - min(xx), max(yy) - min(yy)))