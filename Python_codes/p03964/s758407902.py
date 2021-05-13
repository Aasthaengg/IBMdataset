n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
x, y = ls[0]
for a, b in ls[1:]:
    k = max((x + a - 1) // a, (y + b - 1) // b)
    x, y = k * a, k * b
print(x + y)