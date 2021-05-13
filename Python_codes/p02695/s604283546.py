import itertools
n,m,q=map(int,input().split())
l=[list(map(int,input().split()))for i in range(q)]
y=0
for i in itertools.combinations_with_replacement(range(1,m+1),n):
 x=0
 for a,b,c,d in l:
  if i[b-1]-i[a-1]==c:x+=d
 y=max(y,x)
print(y)