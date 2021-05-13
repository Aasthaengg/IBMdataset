inp = input().split(' ')

N = int(inp[0])
K = int(inp[1])
cnt = 0
for i in range(1, N + 1, 2):
  cnt += 1

if cnt >= K:
  print("YES")
else:
  print("NO")
