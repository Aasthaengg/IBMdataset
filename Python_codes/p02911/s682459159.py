N,K,Q =map(int,input().split())
pts = [0]*N

for i in range(Q):
  a = int(input())
  pts[a-1] += 1
for i in range(N):
  print('Yes' if K-Q+pts[i] >= 1 else 'No')