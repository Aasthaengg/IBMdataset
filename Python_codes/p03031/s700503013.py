N,M = map(int, input().split())

Ks = []
for _ in range(M):
  Ks.append(set(list(map(int, input().split()))[1:]))
  
Ps = list(map(int, input().split()))

rlt = 0
pw = 2**N

for b in range(pw):
  lst = [0]*(M)
  tmp = 0
  for i in range(N):
    if b&(1<<i):
      for j in range(M):
        if i+1 in Ks[j]:
          lst[j] += 1
  for j in range(M):
    if lst[j] % 2 == Ps[j]:
      tmp += 1
  if tmp == M:
    rlt += 1
  
print(rlt)