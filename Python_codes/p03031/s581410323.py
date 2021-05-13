n, m = map(int, input().split())
state = []
for _ in range(m):
  lst = list(map(int, input().split()))
  state.append(lst[1:])
p = list(map(int, input().split()))
ans = 0
for i in range(2**n):
  total = 0
  for j in range(m):
    cnt = 0
    for s in state[j]:
      s -= 1
      if (i >> s) & 1:
        cnt += 1
    cnt %= 2
    if cnt == p[j]:
      total += 1
  if total == m:
    ans += 1
print(ans)