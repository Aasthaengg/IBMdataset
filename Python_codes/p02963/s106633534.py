s = int(input())
x1 = 0
a = 10**9
c = 1
y1 = 0
b = 0
d = 0
t = s//(10**9)
if s%10**9==0:
  d = s//10**9
  print(x1,y1,a,b,c,d)
  exit()
d = t+1
b = 10**9-s%(10**9)
print(x1,y1,a,b,c,d)
