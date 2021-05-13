n,h,w=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
c=0
for j in range(n):
  if h<=l[j][0] and w<=l[j][1]:c+=1
print(c)