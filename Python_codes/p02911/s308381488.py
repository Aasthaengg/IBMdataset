n,k,q=map(int,input().split())
data=[k-q]*n
for i in range(q):
  a=int(input())
  data[a-1]+=1
for i in data:
  if i<=0:
    print('No')
  else:
    print('Yes')