H, W = map(int, input().split(' '))
S = []
for i in range(H):
  S.append(input())
 
dj = [-1, 0, 0, 1]
dk = [0, -1, 1, 0]
flug = []
for j in range(H):
  for k in range(W):
    judge = 'No'
    if S[j][k] == '.':
      judge = 'Yes'
    if S[j][k] == '#':
      for d in range(4):
        if 0 <= j+dj[d] <= H-1:
          if 0 <= k+dk[d] <= W-1:
            if S[j+dj[d]][k+dk[d]] == '#':
              judge = 'Yes'
      if judge == 'No':
        flug.append(0)
if 0 in flug:
  print('No')
else:
  print('Yes')