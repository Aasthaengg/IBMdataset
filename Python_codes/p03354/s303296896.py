a,b=map(int,input().split())
l=list(map(int,input().split()))
root=[i for i in range(a)]
height=[0]*a
group=[set() for i in range(a)]
def find(a):
   f=a
   if a==root[a]:
      return a
   while a!=root[a]:
      a=root[a]
   root[f]=a
   return a
def union(a,b):
   A=find(a)
   B=find(b)
   if A==B:
      return
   if height[A]>height[B]:
      root[B]=root[A]
   else:
      root[A]=root[B]
      if height[A]==height[B]:
         height[B]+=1
for i in range(b):
   x,y=map(int,input().split())
   x-=1;y-=1
   union(x,y)
for i in range(a):
   group[root[find(i)]].add(l[i])
ans=0
for i in range(a):
   if i+1 in group[find(i)]:
      ans+=1
print(ans)