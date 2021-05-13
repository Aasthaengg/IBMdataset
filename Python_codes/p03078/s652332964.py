x,y,z,k=map(int,input().split())
a=sorted(list(map(int,input().split())))[::-1]
b=sorted(list(map(int,input().split())))[::-1]
c=sorted(list(map(int,input().split())))[::-1]
d=[]
for i in a:
  for j in b:
    d+=[i+j]
ans=[]
d=sorted(d)[::-1][:k]
for i in c:
  for j in d:
    ans+=[i+j]
print(*sorted(ans)[::-1][:k],sep='\n')