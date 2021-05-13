H, W = map(int,input().split(' '))
S = []
for i in range(H):
  S.append(input())
for j in range(H):
  answer = list(S[j])
  for k in range(W):
    cnt = 0
    if S[j][k] == '#':
      pass
    if S[j][k] == '.':
      if j-1 >= 0:
        if k-1 >= 0:
          if S[j-1][k-1] == '#':
            cnt += 1
        if S[j-1][k] == '#':
          cnt += 1
        if k+1 <= W-1:
          if S[j-1][k+1] == '#':
            cnt += 1
      if k-1 >= 0:
        if S[j][k-1] == '#':
          cnt += 1
      if k+1 <= W-1:
        if S[j][k+1] == '#':
          cnt += 1
      if j+1 <= H-1:
        if k-1 >= 0:
          if S[j+1][k-1] == '#':
            cnt += 1
        if S[j+1][k] == '#':
          cnt += 1
        if k+1 <= W-1:
          if S[j+1][k+1] == '#':
            cnt += 1
      answer[k] = str(cnt)
  print(''.join(answer))