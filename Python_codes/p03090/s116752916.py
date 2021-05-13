N = int(input())
ans = set()
for i in range(1, N+1):
  for j in range(i+1, N+1):
    ans.add((i, j))

if N % 2 == 1: # 奇数
  for i in range(1, N+1):
    j = N - i
    ans.discard((i, j))
else: # 偶数
  for i in range(1, N+1):
    j = N + 1 - i
    ans.discard((i, j))

print(len(ans))
for a in ans:
  print(*a)