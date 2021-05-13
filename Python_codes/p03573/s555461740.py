A,B,C=map(int,input().split())
a,b=min(A,B,C),max(A,B,C)
c=A+B+C-a-b
if a==b:
  print(c)
elif a==c:
  print(b)
else:
  print(a)