n=int(input())
l=list(map(int,input().split()))

if n<=2:
  print(1)
  exit()
  
cnt=0

if l[0]>l[1]:
  ans="low"
elif l[0]<l[1]:
  ans="high"
else:
  ans="even"
  
for i in range(2,n):
  if l[i-1]>l[i] and (ans=="low" or ans=="even"):
    ans="low"
  elif l[i-1]<l[i] and (ans=="high" or ans=="even"):
    ans="high"
  elif l[i-1]==l[i]:
    continue
  else:
    cnt+=1
    ans="even"
    
print(cnt+1)
