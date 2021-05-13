res=0
for i in range(int(input())):
  x,u=input().split()
  x=float(x)
  res+=x if u>'C'else 380000*x
print(res)