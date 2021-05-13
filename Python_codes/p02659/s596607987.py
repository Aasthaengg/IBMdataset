a, b = map(float, input().split())
a = int(a)
x = int(100 * b + 0.5)
c = a * x
c = c // 100
print(int(c))
