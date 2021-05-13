N = int(input())

P = []
for _ in range(N):
  x,l = list(map(int, input().split()))
  P.append((x+l, x-l))
  
P.sort()
rw = P[0][0]
ans = 1
for i in range(1,N):
  r,l = P[i]
  if l < rw:
    continue
  else:
    rw = r
    ans += 1
    
print(ans)
