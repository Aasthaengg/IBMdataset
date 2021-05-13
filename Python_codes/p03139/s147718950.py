n, a, b = map(int, input().split())
x = min(a, b)
y = - ( n - a - b )
y = 0 if y < 0 else y
print(x,y)