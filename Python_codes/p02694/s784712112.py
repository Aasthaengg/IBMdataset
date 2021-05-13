import math

X = int(input())

kane = 100
n = 0
while kane < X:
    n += 1
    kane = kane * 101
    kane = kane // 100

    #print(kane)
print(n)