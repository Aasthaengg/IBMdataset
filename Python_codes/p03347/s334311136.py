n=int(input())
if int(input())!=0:
  print(-1)
  exit()
b=0
c=0

for i in range(n-1):
  a=int(input())
  if a>b+1:
    print(-1)
    exit()
  else:
    if a==b+1:
      c+=1
    else:
      c+=a  
  b=a
print(c)