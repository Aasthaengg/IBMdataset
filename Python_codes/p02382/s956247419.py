import math
def mink(x,y,p):
    return (sum([math.fabs(_x - _y)**p for _x, _y in zip(x,y)]))**(1/p)
def mink_i(x,y):
    return max([math.fabs(_x - _y) for _x, _y in zip(x,y)])
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
print(mink(x,y,1))
print(mink(x,y,2))
print(mink(x,y,3))
print(mink_i(x,y))

