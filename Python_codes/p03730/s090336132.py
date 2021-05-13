a,b,c=map(int,input().split())
x=1
fl=False
while x<b:
  if x*a%b==c:
    fl=True
    break
  x+=1
if fl:
  print("YES")
else:
  print("NO")