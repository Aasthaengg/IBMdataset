#conding utf-8
x,y,z,K=map(int,input().split())
a=list(map(int,input().split())) 
b=list(map(int,input().split())) 
c=list(map(int,input().split())) 

a.sort()
b.sort()
c.sort()
a.reverse()
b.reverse()
c.reverse()

ans=[]

for i in range(len(a)):
  for j in range(len(b)):
    if (i+1)*(j+1)>K:
      break
    for k in range(len(c)):
      if (i+1)*(j+1)*(k+1)>K:
        break
      ans.append(a[i]+b[j]+c[k])
    
ans.sort()
ans.reverse()

for i in range(K):
  print(ans[i])