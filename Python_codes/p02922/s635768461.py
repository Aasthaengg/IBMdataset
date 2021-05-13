import sys
a,b=map(int,input().split())
if b==1:
  print("0")
  sys.exit()
p=1
ans=0
for i in range(0,20):
  p+=a-1
  ans+=1
  if p>=b:
    print(ans)
    sys.exit()