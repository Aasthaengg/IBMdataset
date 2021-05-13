def koch(n, a_x, a_y, b_x, b_y):
  if n == 0:
    return
 
  th = math.pi*60.0/180.0
 
  s_x = (2.0*a_x + 1.0*b_x)/3.0
  s_y = (2.0*a_y + 1.0*b_y)/3.0
  t_x = (1.0*a_x + 2.0*b_x)/3.0
  t_y = (1.0*a_y + 2.0*b_y)/3.0
  u_x = (t_x - s_x)*math.cos(th) - (t_y - s_y)*math.sin(th) + s_x
  u_y = (t_x - s_x)*math.sin(th) + (t_y - s_y)*math.cos(th) + s_y
 
  koch(n-1, a_x, a_y, s_x, s_y)
  print '%.8f %.8f' % (s_x, s_y)
  koch(n-1, s_x, s_y, u_x, u_y)
  print '%.8f %.8f' % (u_x, u_y)
  koch(n-1, u_x, u_y, t_x, t_y)
  print '%.8f %.8f' % (t_x, t_y)
  koch(n-1, t_x, t_y, b_x, b_y)
 
 

import math
n = input()
a_x = 0.0
a_y = 0.0
b_x = 100.0
b_y = 0.0
 
print '%.8f %.8f' % (a_x, a_y)
koch(n, a_x, a_y, b_x, b_y)
print '%.8f %.8f' % (b_x, b_y)