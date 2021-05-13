import math as mt

x1 , y1 , x2,y2 = list(map(float, input().split()))
a = pow(x2 - x1,2 )
b = pow(y2 - y1,2)
c = mt.sqrt(a+b)
print(f'{c:.8f}')

