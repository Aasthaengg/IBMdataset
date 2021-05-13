N, K = map(int, input().split())
l = []
for i in range(N):
  a, b = map(int, input().split())
  l.append([a, b])
  
l.sort()
cnt = 0
ans = 0
i = 0
while cnt < K:
  ans = l[i][0]
  cnt += l[i][1]
  i += 1
print(ans)