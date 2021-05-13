ip=lambda:int(input())
n=ip()
p=[ip() for _ in range(n)]
d=[0]*(n+1)
for q in p:
  d[q]+=d[q-1]+1
print(n-max(d))
