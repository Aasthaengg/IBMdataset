a,b,c=map(int,input().split())
flag=0
for i in range(b):
  if (a*(i+1)%b==c):
    print("YES")
    flag=1
    break
    
if (flag==0):
  print("NO")