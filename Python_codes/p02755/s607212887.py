import math

a, b = map(int,input().split())

flg = False
for i in range(0, 1011):
    x = math.floor(0.08 * i)
    y = math.floor(0.10 * i)
    if x == a and y == b:
        flg = True
        break
print(i) if flg else print(-1)