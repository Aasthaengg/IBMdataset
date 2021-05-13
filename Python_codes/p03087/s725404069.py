n,q=map(int,input().split())
s=input()
a=[]
for i in range(len(s)-1):
  a.append(s[i:i+2])
b=[0]
for i in a:
  b.append(b[-1])
  if i=='AC':
    b[-1]+=1

for i in range(q):
  l,r=map(int,input().split())
  print(b[r-1]-b[l-1])