H, W = map(int,input().split(' '))
S = []
dj = [-1, -1, -1, 0, 0, 1, 1, 1]
dk = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(H):
  S.append(input())
for j in range(H):
  answer = list(S[j])
  for k in range(W):
    cnt = 0
    if S[j][k] == '#':
      pass
    if S[j][k] == '.':
      for d in range(8):
        if 0 <= j+dj[d] <= H-1:
          if 0 <= k+dk[d] <= W-1:
            if S[j + dj[d]][k+dk[d]] == '#':
              cnt += 1
      answer[k] = str(cnt)
  print(''.join(answer))