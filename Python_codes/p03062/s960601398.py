n=int(input())
a=[*map(int,input().split())]
c=0
l=[]
for i in a:
  if i<0: c+=1
  l+=[abs(i)]
print(sum(l)-[0,min(l)*2][c%2])