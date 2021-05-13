H,W,K=map(int,input().split())
s=[[int(x) for x in list(input())] for _ in range(H)]
ans = H*W
for h in range(2**(H-1)):
  parts = list()
  upper = 0
  cnt = 0
  inv_flg = 0
  for j in range(H-1):
    if h >> j & 1:
      cnt += 1
      appending = [sum([s[y][x] for y in range(upper, j+1)]) for x in range(W)]
      if any([x> K for x in appending]):
        inv_flg = 1
        break
      parts.append(appending)
      upper = j+1
  else:
    appending = [sum([s[y][x] for y in range(upper, H)]) for x in range(W)]
    if any([x > K for x in appending]):
      inv_flg = 1
    else:
      parts.append(appending)
  if inv_flg:
    continue
  # 貪欲
  summary = [0]*len(parts)
  for i in range(W):
    temp_sum = [summary[j] + parts[j][i] for j in range(len(parts))]
    for ts in temp_sum:
      if ts > K:
        cnt += 1
        summary = [parts[j][i] for j in range(len(parts))]
        break
    else:
      summary = temp_sum
  ans = min(ans, cnt)
print(ans)
