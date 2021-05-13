n, x = [int(i) for i in input().split()]
xs = [int(input()) for i in range(n)]

tmp = x - sum(xs)
y = min(xs)

print(tmp // y + n)