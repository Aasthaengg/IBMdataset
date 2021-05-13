n,m=map(int,input().split())
a=[0 for _ in range(m)]
for x in range(n):
  e=list(map(int,input().split()))
  e.remove(e[0])
  for p in e:
    a[p-1]+=1
    
print(a.count(n))