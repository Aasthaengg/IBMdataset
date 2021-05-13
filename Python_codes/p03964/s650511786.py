import math
n=int(input())
A=B=1
for i in range(n):
    x,y=[int(i) for i in input().split()]
    n=max(-(-A//x),-(-B//y))
    A=n*x
    B=n*y
print(A+B)