n,k=map(int,input().split())
l=[0] * n
for _ in range(k):
  d=int(input())
  kashi=list(map(int, input().split()))
  for kk in kashi:
    l[kk-1]=1
print(l.count(0))