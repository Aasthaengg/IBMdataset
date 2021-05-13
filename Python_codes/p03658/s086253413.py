n,k=map(int, input().split())
l=list(map(int, input().split()))
l.sort()
t=0
for i in range(k):
  t+=l[n-1-i]
print(t)
