
n=int(input())
t=list(map(int,input().split()))
m=int(input())
d=[]
for _ in range(m):
  d.append(list(map(int,input().split())))
  
ans=[sum(t)-t[x[0]-1]+x[1] for x in d]
for x in ans:
  print(x)