n=int(input())
l=[]
for i in range(n):
  a,b=list(map(int,input().split()))
  l.append([a+b,a,b])

l.sort()
l.reverse()
s=0
for i in range(0,n,2):
  s+=l[i][1]
for i in range(1,n,2):
  s-=l[i][2]
print(s)