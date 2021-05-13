N, M = map(int, input().split())
newcount = [100000000 for _ in range(2**N)]
newcount[0] = 0
bi = [1,2,4,8,16,32,64,128,256,512,1024,2048]
for k in range(M):
  a, b = map(int, input().split())
  c = list(map(int, input().split()))
  bit = 0
  for k in range(b):
    bit += bi[c[k]-1]
  count = tuple(newcount)
  for k in range(2**N):
    now = bit|k
    newcount[now] = min(newcount[now], a+count[k])
if newcount[-1] < 10**7:
  print(newcount[-1])
else:
  print(-1)