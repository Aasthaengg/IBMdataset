n,k,q=map(int,input().split())
a=[int(input()) for _ in range(q)]
b=[k-q]*n
for x in a:
  b[x-1]+=1
for x in b:
  if x<=0:
    print('No')
  else:
    print('Yes')
