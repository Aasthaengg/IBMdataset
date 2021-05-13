n,q=map(int,input().split())
s=input()
a=[0]
current=0
for i in range(n-1):
  if s[i]=='A' and s[i+1]=='C':
    current+=1
  a.append(current)
for i in range(q):
  x,y=map(int,input().split())
  if y==1:
    print(0)
    continue
  print(a[y-1]-a[x-1])