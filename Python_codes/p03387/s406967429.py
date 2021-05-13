a,b,c = map(int,input().split())
s = a+b+c
m = max(a,b,c)
if s%2 == 0 and (m*3)%2 == 0:
  print(((m*3)-s)//2)
elif s%2 != 0 and (m*3)%2 != 0:
  print(((m*3)-s)//2)
else:
  print(((m+1)*3-s)//2)