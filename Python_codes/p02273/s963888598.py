import math

def show_vertex(x, y):
  print("%.8f %.8f" % (x, y))

def koch(x0, y0, x1, y1, n):
  if n ==0:
    show_vertex(x0, y0)
  else:
    c1 = [x0 + (x1-x0)/3, y0 + (y1-y0)/3]
    c3 = [x0 + 2*(x1-x0)/3, y0 + 2*(y1-y0)/3]
    c2 = [(x0 + x1)/2 + ((y0-y1)*math.sin(math.pi/3))/3, (y0 + y1)/2 + ((x1-x0)*math.sin(math.pi/3))/3]
    koch(x0,y0, c1[0],c1[1], n-1)
    koch(c1[0],c1[1], c2[0],c2[1], n-1)
    koch(c2[0],c2[1], c3[0],c3[1], n-1)
    koch(c3[0],c3[1], x1,y1, n-1)

N = int(input())
koch(0, 0, 100, 0, N)
show_vertex(100, 0)
