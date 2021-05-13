n,q=map(int, input().split())
s=input()

a=[0]*(n+1)
tmp=0
for i in range(1,n+1):
  if s[i-1:i+1]=="AC":
    a[i]=tmp+1
    tmp=a[i]
  else:
    a[i]=tmp
#print(a)

for _ in range(q):
  l,r=map(int, input().split())
  print(a[r-1] - a[l-1])