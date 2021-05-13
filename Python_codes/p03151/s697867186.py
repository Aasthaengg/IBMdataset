n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
  if a[i]>b[i]:
    c.append(a[i]-b[i])
  elif a[i]<b[i]:
    d.append(b[i]-a[i])
c.sort(reverse=True)
if sum(c)<sum(d):
  print(-1)
elif sum(c)==sum(d):
  print(len(c)+len(d))
else:
  ans=0
  if len(c)==1:
    print(1+len(d))
  else:
    for i in range(len(c)):
      if sum(c[:i])>=sum(d):
        ans=i
        break
    print(ans+len(d))