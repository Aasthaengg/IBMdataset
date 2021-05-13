from itertools import product
n,*B=map(int,input().split())
A=[int(input()) for i in range(n)]
s=10**9
for P in product([0,1,2,3],repeat=n):
  if {0,1,2}<=set(P):
    m=[0,0,0]
    for x,y in zip(P,A):
      if x!=3:
        m[x]+=y
    t=sum(abs(m-y) for m,y in zip(m,B))
    l=sum(1 for j in P if j!=3)-3
    s=min(s,t+l*10)
print(s)