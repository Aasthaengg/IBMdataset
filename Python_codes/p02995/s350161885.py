a,b,c,d=map(int,input().split())

def calc_div_num(a,b,x):
  return b//x - (a-1)//x

num_c = calc_div_num(a, b, c)
num_d = calc_div_num(a, b, d)

import numpy as np
import math
#lcd = np.lcm(c, d)
lcd = c*d/math.gcd(c,d)
num_lcd = calc_div_num(a, b, int(lcd))

result = b-a+1 - (num_c+num_d-num_lcd)
print(result)