import math
x1, y1, x2, y2 = map(float,input().split())
a = math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
print(f'{a:.8f}')
