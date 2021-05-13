a,b,c,d=map(int,input().split())

def calc_div_num(a,b,x):
  return b//x - (a-1)//x

num_c = b//c - (a-1)//c
num_d = b//d - (a-1)//d

import math
lcd = int(c * d / math.gcd(c,d))
num_lcd = b//lcd - (a-1)//lcd

result = b-a+1 - (num_c+num_d-num_lcd)
print(result)