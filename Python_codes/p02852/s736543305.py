n,m=map(int,input().split())
s=input()
a=[]
x=n
while x>0:
  f=1
  for i in range(min(m,x),0,-1):
    if int(s[x-i]):
      continue
    else:
      a.append(i)
      x-=i
      f=0
      break
  if f:
    x=0
    a=[-1]
a=a[::-1]
print(*a)