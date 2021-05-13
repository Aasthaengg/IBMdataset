x, y = map(int, input().split())
B = 0
if x == -y:
    print(1)
elif x <= y:
    if x < 0 and y > 0:
        B = 1
    print(B + abs(abs(y)-abs(x)))
elif y < x:
    if x >= 0 and y <= 0:
        print(1 + abs(x+y))
    else:
        print(2 + abs(y-x))
"""
y = -x : print(1)

x <= y : print(y-x)
(ex: x=3, y=10)
(ex: x=-3, y=-1)
(ex: x=-3, y=1)

(ex: x=-3, y=50) : 

y < x : 2 + |y-x|
(ex: x=20, y=10)
(ex: x=20, y=-100)
(ex: x=-20, y=-100)

"""