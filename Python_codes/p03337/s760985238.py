a, b = map(int, input().split())
x = max(a*b, max(a+b, a-b))
print(x)
