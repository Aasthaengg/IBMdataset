n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

x = 1
y = 1
for i in range(n):
    a = ab[i][0]
    b = ab[i][1]

    m = max(-(-x // a), -(-y // b))
    x = m * a
    y = m * b
print(x + y)
