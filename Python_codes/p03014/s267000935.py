H, W = map(int, input().split())
S = []
l1 = []
for i in range(H):
  s = str(input())
  S.append(s)
  tmp = []
  cnt = 0
  flag = False
  for j in s:
    if flag:
      if j == '.':
        cnt += 1
      else:
        for k in range(cnt):
          tmp.append(cnt)
        cnt = 0
        tmp.append(0)
        flag = False
    else:
      if j == '.':
        flag = True
        cnt += 1
      else:
        tmp.append(0)
  if cnt > 0:
    for k in range(cnt):
      tmp.append(cnt)
  l1.append(tmp)

l2 = []
for i in range(W):
  tmp = []
  cnt = 0
  flag = False
  for j in range(H):
    x = S[j][i]
    if flag:
      if x == '.':
        cnt += 1
      else:
        for k in range(cnt):
          tmp.append(cnt)
        cnt = 0
        tmp.append(0)
        flag = False
    else:
      if x == '.':
        flag = True
        cnt += 1
      else:
        tmp.append(0)
  if cnt > 0:
    for k in range(cnt):
      tmp.append(cnt)
  l2.append(tmp)

ans = [[0]*W for i in range(H)]
m = 0
for i in range(H):
  for j in range(W):
    if (l1[i][j]>0) and (l2[j][i]>0):
      ans[i][j] = l1[i][j] + l2[j][i] - 1
    else:
      ans[i][j] = l1[i][j] + l2[j][i]
    m = max(m, ans[i][j])
print(m)