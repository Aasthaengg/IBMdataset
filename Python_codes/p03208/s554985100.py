N, K = map(int, input().split())
hs = []
for _ in range(N):
  hs.append(int(input()))
hs.sort()
  
start, end = 0, K-1
ans = float('inf')
while end < N:
  ans = min(ans, hs[end]-hs[start])
  start += 1
  end += 1
  
print(ans)