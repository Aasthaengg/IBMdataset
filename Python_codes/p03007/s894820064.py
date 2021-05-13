n=int(input())
l=list(map(int,input().split()))
l.sort()
if l[0]>=0 :
  print(sum(l)-2*l[0])
  for i in range(1,n-1):
    print(l[0],l[i])
    l[0]-=l[i]
  print(l[-1],l[0])
elif l[-1]<0:
  print(abs(sum(l)-2*l[-1]))
  for i in range(n-1):
    print(l[-1],l[i])
    l[-1]-=l[i]
else:
  cnt=0
  i=0
  while l[i]<0:
    cnt+=1
    if l[i+1]>=0:
      break
    i+=1
  ans=0
  for j in range(n):
    ans+=abs(l[j])
  print(ans)
  for j in range(n-2-i):
    print(l[0],l[i+j+1])
    l[0]-=l[i+j+1]
  for j in range(i+1):
    print(l[-1],l[j])
    l[-1]-=l[j]
    
