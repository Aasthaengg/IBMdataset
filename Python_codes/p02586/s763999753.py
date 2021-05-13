R, C, K = map(int, input().split())
V = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(K):
  r, c, v = map(int, input().split())
  V[r-1][c-1] = v
M = [0] * R * C * 4 
# M[r*C*4 + c*4 + i]
# M[(r-1)*C*4 + c*4 + i]
# M[r*C*4 + (c-1)*4 + i]
# M[r][c][count in column (c)]
for r in range(R):
  for c in range(C):
    for n_pick in [0, 1] if V[r][c] else [0]:
      M[r*C*4 + c*4 +n_pick] = max(M[r*C*4 + c*4 +n_pick], n_pick*V[r][c])
      if r > 0:
        for n_prev in range(4):
          #print('R++', r, c, n_pick, n_prev)
          if M[(r-1)*C*4 + c*4 +n_prev] > 0 or n_prev == 0:
            M[r*C*4 + c*4 +n_pick]=max(M[r*C*4 + c*4 +n_pick],
              M[(r-1)*C*4 + c*4 +n_prev] + n_pick*V[r][c])
      if c > 0:
        for n_prev in range(4 - n_pick):
          #print('C++', r, c, n_pick, n_prev)
          if  M[r*C*4 + (c-1)*4 +n_prev]  > 0 or n_prev == 0:
            M[r*C*4 + c*4 +n_prev+n_pick]=max(M[r*C*4 + c*4 + n_prev+n_pick],
              M[r*C*4 + (c-1)*4 +n_prev] + n_pick*V[r][c])
    #print(candidates)
    #print(r, c, candidates, M)
    #for i in range(4):
    #  M[r][c][i] = max(candidates[i])
    #print(r, c, M)
#print(V, M)
print(max(M[((R-1)*C*4 + (C-1) *4):((R-1)*C*4 + (C-1) *4+4)]))
