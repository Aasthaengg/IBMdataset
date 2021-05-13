import collections
N,x,y=map(int,input().split())
lit=[]
for i in range(1,N+1):
  for j in range(i+1,N+1):
     lit.append(min(abs(i-j),abs(x-j)+abs(y-i)+1,abs(y-j)+abs(x-i)+1))
a=collections.Counter(lit)
for i in range(1,N):
  print(a[i])