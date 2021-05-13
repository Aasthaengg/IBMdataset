import math
x = int(input())

sq_x = int(x ** 0.5)
ans = 1
for i in range(2, sq_x + 1):
    t = i
    while t <= x:
        ans = max(ans, t)
        t *= i

print(ans)

"""
最初は
p = int(math.log(x, i))
でいけるかと思ったが
math.log(1000,10)のとき 2.999..みたいな値になってしまい，誤差がある
"""