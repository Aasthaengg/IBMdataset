from collections import deque

N, M = map(int, input().split())
k = deque()
s = deque()
for _ in range(M):
    inp = list(map(int, input().split()))
    k.append(inp[0])
    s.append(inp[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
  all_on = True
  for m_i in range(M):
    swon = 0
    for s_i in s[m_i]:
      if i>>(s_i-1)&1:
        swon += 1
    
    if swon%2 != p[m_i]: #電球がOFFだったら
      all_on = False
      break
  
  if all_on: ans += 1

print(ans)
