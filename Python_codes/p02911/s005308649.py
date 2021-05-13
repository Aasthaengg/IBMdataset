from collections import defaultdict
N, K, Q = map(int,input().split())
d = defaultdict(int)
for _ in range(Q):
  a = int(input())
  d[a]+=1
for i in range(1,N+1):
  if K-Q+d[i]>0:
    print('Yes')
  else:
    print('No')