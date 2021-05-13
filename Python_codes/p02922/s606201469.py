a,b=input().split()
a=int(a)
b=int(b)
if b==1:
  print(0)
elif a>=b:
  print(1)
else:
  if (b-a)%(a-1)==0:
    print(int((b-a)/(a-1))+1)
  else:
    print(int((b-a)/(a-1))+2)