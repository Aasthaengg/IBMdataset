N, K, Q = map(int, input().split())

start = [K - Q] * N

for i in range(Q):
  a = int(input())
  start[a-1] += 1
     
for i in range(N):
  if start[i] > 0:
    print('Yes')
  else:
    print('No')