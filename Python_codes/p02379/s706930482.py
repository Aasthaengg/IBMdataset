x_1,y_1,x_2,y_2=map(float,input().split())

import math
x=(x_2-x_1)**2
y=(y_2-y_1)**2

l=math.sqrt(x+y)
print('{:.16g}'.format(l))
