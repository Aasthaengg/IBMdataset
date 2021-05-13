a=[0]*3
b=[0]*3

a[0],b[0]=map(int,input().split())
a[1],b[1]=map(int,input().split())
a[2],b[2]=map(int,input().split())

d=dict()
c=a+b
for i in c:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1

mini=100
maxi=0
for j in d:
  mini=min(mini,d[j])
  maxi=max(maxi,d[j])


if mini==1 and maxi==2:
  print("YES")
else:
  print("NO")