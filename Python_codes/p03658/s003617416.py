n,k=map(int,input().split())
a=list(map(int, input().split()))
l=0
for i in range(k):
  l+=max(a)
  a.remove(max(a))

print(l)