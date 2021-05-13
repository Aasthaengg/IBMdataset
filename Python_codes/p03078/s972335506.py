#conding utf-8
x,y,z,k=map(int,input().split())
a=list(map(int,input().split())) 
b=list(map(int,input().split())) 
c=list(map(int,input().split())) 

ab=[]
ans=[]
for i in range(len(a)):
  for j in range(len(b)):
    ab.append(a[i]+b[j])
    
ab.sort()
ab.reverse()
del ab[k:]

c.sort()
c.reverse()

for i in range(len(ab)):
  for j in range(len(c)):
    ans.append(ab[i]+c[j])
    
ans.sort()
ans.reverse()

for i in range(k):
  print(ans[i])