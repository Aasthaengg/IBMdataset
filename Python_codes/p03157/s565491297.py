H, W = map(int, input().split())
S = [['.']*(W+2)] + [['.'] + list(input()) + ['.'] for _ in range(H)] + [['.']*(W+2)]
for i in range(1, H+1):
  S[i][0] = S[i][1]
  S[i][-1] = S[i][-2]
for i in range(1, W+1):
  S[0][i] = S[1][i]
  S[-1][i] = S[-2][i]
S[0][0] = S[0][1]
S[-1][0] = S[-2][0]
S[0][-1] = S[0][-2]
S[-1][-1] = S[-2][-1]
V = [[0 for _ in range(W+2)] for i in range(H+2)]
num = 0
for i in range(1, H+1):
  for j in range(1, W+1):
    if S[i][j] == '#' and V[i][j] == 0:
      V[i][j] = 1
      p = [[i, j]]
      cnt = 1
      pnt = 0
      D = {'.': 0, '#': 0}
      D[S[i][j]] = 1
      while pnt < cnt:
        n = cnt
        for k in range(pnt, cnt):
          x = p[k][:]
          y = S[x[0]][x[1]][:]
          if S[x[0]-1][x[1]] != y and V[x[0]-1][x[1]] == 0:
            V[x[0]-1][x[1]] = 1
            p.append([x[0]-1, x[1]])
            D[S[x[0]-1][x[1]]] += 1
            cnt += 1
          if S[x[0]+1][x[1]] != y and V[x[0]+1][x[1]] == 0:
            V[x[0]+1][x[1]] = 1
            p.append([x[0]+1, x[1]])
            D[S[x[0]+1][x[1]]] += 1
            cnt += 1
          if S[x[0]][x[1]-1] != y and V[x[0]][x[1]-1] == 0:
            V[x[0]][x[1]-1] = 1
            p.append([x[0], x[1]-1])
            D[S[x[0]][x[1]-1]] += 1
            cnt += 1
          if S[x[0]][x[1]+1] != y and V[x[0]][x[1]+1] == 0:
            V[x[0]][x[1]+1] = 1
            p.append([x[0], x[1]+1])
            D[S[x[0]][x[1]+1]] += 1
            cnt += 1
        pnt = n
      num += D['.'] * D['#']
print(num)