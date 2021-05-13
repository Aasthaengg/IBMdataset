n = int(input())
a = []
for i in range(n):
  tmp = list(map(int, input().split()))
  a.append(tmp[2:])
ans = [-1 for _ in range(n + 1)]
ans[1] = 0
que = [1]
while len(que) > 0:
  current = que.pop(0)
  if len(a[current - 1]) == 0:
    continue
  for next in a[current - 1]:
    if ans[next] == -1:
      que.append(next)
      ans[next] = ans[current] + 1
for i in range(1, n + 1):
  print(i, ans[i])
    
