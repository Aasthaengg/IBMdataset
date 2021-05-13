n,k=map(int,input().split())
s=input()
s='x'+s
l=[0]*n
for i in range(n):
  if s[i:i+2]=='AC':
    l[i]=l[i-1]+1
  else:
    l[i]=l[i-1]
for i in range(k):
  a,b=map(int,input().split())
  print(l[b-1]-l[a-1])