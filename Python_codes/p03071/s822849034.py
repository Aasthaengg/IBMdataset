x, y = map(int,input().split())
if x < y:
    x, y = y, x
m = x
x -= 1
print(m + max(x, y))