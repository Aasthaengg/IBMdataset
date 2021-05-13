N, M = map(int, input().split())
newcount = [float('inf') for _ in range(2**N)]
newcount[0] = 0

for k in range(M):
  a, b = map(int, input().split())
  c = list(map(int, input().split()))
  bit = 0
  for k in range(b):
    bit += 2**(c[k]-1)
  count = tuple(newcount)
  for k in range(2**N):
    now = bit|k
    newcount[now] = min(newcount[now], a+count[k])
count = newcount
if count[-1] < 10**6:
  print(count[-1])
else:
  print(-1)

