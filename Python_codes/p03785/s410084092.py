N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]

T.sort()

ans = 0

oko = 0
bus = False
cnt = 0
for i in range(N):
  t = T[i]
  
  if not bus:
    ans += 1
    bus = True
    oko = t + K
    cnt += 1
    continue
    
  if t <= oko:
    if cnt < C:
      cnt += 1
    else:
      bus = True
      oko = t + K
      cnt = 1
      ans += 1
  else:
    cnt = 1
    bus = True
    ans += 1
    oko = t + K
    
print(ans)
      
