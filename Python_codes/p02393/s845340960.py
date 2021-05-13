
num = input().split()
 
a = int(num[0])
b = int(num[1])
c = int(num[2])
 
if a <= b <= c :
  print(a,b,c);
elif a <= c <= b :
  print(a,c,b);
elif b <= a <= c:
  print(b,a,c)
elif b <= c <= a:
  print(b,c,a)
elif c <= a <= b:
  print(c,a,b)
else:
  print(c,b,a)