n,k,q=map(int,input().split())
cnt=[0]*(n+1)
for _ in range(q):
  cnt[int(input())]+=1
for i in range(1,n+1):
  if k-(q-cnt[i])>0:
    print('Yes')
  else:
    print('No')