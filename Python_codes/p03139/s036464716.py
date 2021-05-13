n, a, b = map(int, input().split(' '))

x = min(a, b)
if (a + b) > n:
    y = (a + b) - n
else:
    y = 0 

print(x, y)