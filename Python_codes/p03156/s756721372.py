n = int(input())
a,b = map(int, input().split())
l = map(int, input().split())
x,y,z = 0,0,0
for i in l:
  if i<=a:
    x+=1
  elif i>a and i<=b:
    y+=1
  elif i>b:
    z += 1
print(min(x,min(y,z)))