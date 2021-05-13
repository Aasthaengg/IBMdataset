N, X = map(int,input().split())
S = map(int,input().split())
S = sorted(S)
cnt = 0

for s in S:
  X -= s
  if X >= 0:
    cnt += 1
  else:
    break

if X > 0:
  cnt -= 1
    
print(cnt)

