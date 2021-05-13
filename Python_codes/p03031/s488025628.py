N, M = map(int,input().split())
state = []
for _ in range(M):
  lst = list(map(int, input().split()))
  state.append(lst[1:])#switch numbers each denkyu
p = list(map(int, input().split()))#numbers switches on %2 == pi 
ans = 0
for i in range(2**N):
  total = 0
  for j in range(M):
    cnt = 0
    for s in state[j]:
      s -= 1
      if (i >> s) & 1:#全スイッチのパターン一つ一つについて、各電球の各スイッチがオンになっているか
        cnt += 1
    cnt %= 2
    if cnt == p[j]:
      total += 1
    else:
      break
  if total == M:
    ans += 1
print(ans)