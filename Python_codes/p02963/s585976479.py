# (0,0),(a,b),(c,d)
# (10**9, 1)(x,y)
# 10**9 * y - x == S
# S = 10**9 * a + bとおくと
# y = a + 1
# x = 10**9- b

S=int(input())
if S==10**18:
  print(0,0,10**9,0,0,10**9)
  exit(0)
DIV=10**9
a = S//DIV
b = S%DIV
x = 10**9-b
y = a + 1
if x>10**9:
  print(x)
if y>10**9:
  print(y)
print(0,0,10**9,1,x,y)
