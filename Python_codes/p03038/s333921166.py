n,m=map(int,input().split())
a=list(map(int,input().split()))

d=[]
for x in a:
  s=[1,x]
  d.append(s)
  
for _  in range(m):
  b=list(map(int,input().split()))
  d.append(b)
  
d.sort(key=lambda x:x[1],reverse=True)
  
ch=0
ans=0
for f in d:
  p,q=f[0],f[1]
  if ch==n:
    break
  else:
    if ch+p>=n:
      ans+=q*(n-ch)
      break
    else:
      ans+=p*q
      ch+=p
      
print(ans)