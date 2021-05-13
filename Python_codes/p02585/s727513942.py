n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
dic = {}
for i in range(1, n+1):
  dic[i] = [p[i-1], c[i-1]]
INF = 10**20
ans = -INF
for j in range(1, n+1):
  state = [True] * 5001
  max_score = -INF
  max_idx = 0
  score = 0
  now = dic[j][0]
  cnt = 0
  lst = []
  flg = True
  for _ in range(k):
    if not state[now]:
      flg = False
      break
    score += dic[now][1]
    cnt += 1
    if max_score < score:
      max_score = score
      max_idx = cnt
    lst.append(score)
    state[now] = False
    now = dic[now][0]
  if score <= 0 or flg:
    ans = max(max_score, ans)
  else:
    q = k // cnt
    r = k % cnt
    if r >= max_idx:
      x = score * q + max_score
      ans = max(ans, x)
    else:
      if q >= 1:
        if r == 0:
          x = score * (q - 1) + max_score
          ans = max(ans, x)
        else:
          x = score * (q - 1) + max_score
          y = score * q + max(lst[:r])
          ans = max(ans, x, y)
      else:
        ans = max(ans, max_score)
print(ans)
    
