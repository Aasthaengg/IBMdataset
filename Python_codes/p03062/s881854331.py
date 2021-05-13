n=int(input())
a=[*map(int,input().split())]
b=c=0
l=[]
for i in a:
  if i==0:
    b=1
  if i<0:
    c+=1
  l.append(abs(i))
print(sum(l)-[0,min(l)*2][c%2 and b<1])