n=int(input())
s=[int(i)for i in input().split()]
d=int(input())
a=0
for i in range(d):
  x,y=map(int,input().split())
  x-=1
  a=s[x]
  s[x]=y
  print(sum(s))
  s[x]=a