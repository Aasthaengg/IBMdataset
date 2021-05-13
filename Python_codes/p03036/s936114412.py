# 127 B

r, D, x1 = map(int, input().split())

for i in range(10):
    x2 = (r * x1) - D
    print(x2)
    x1 = x2
