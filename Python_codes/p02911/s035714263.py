n,k,q=list(map(int,input().split()))
a=[0 for _ in range(n)]
for i in range(q):
  x=int(input())
  a[x-1] += 1
w=q-k+1
for i in range(n):
  if a[i] >= w:
    print('Yes')
  else:
    print('No')
