n,k=map(int, input().split())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort()
t=0
for i in range(n):
  t+=a[i][1]
  if t>=k:
    print(a[i][0])
    break