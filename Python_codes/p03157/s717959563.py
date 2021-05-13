H,W = list(map(int, input().split()))

S = [[1 if s=='#' else -1 for s in input()] for _ in range(H)]

def surround(matrix, fill=0):
  if not isinstance(matrix, list):
    raise
  if not all([isinstance(rows, list) for rows in matrix]):
    raise
  if not all([len(rows)==len(matrix[0]) for rows in matrix]):
    raise
  r = len(matrix)
  c = len(matrix[0])
  new_matrix = [[fill]*(c+2)] + [[fill]+rows+[fill] for rows in matrix] + [[fill]*(c+2)]
  return new_matrix

S = surround(S, 0)
# 黒: 1 白:-1 枠:0

from itertools import product
to_visit = set(list(product(range(1,H+1), range(1, W+1))))


from collections import deque

answer = 0
while to_visit:
  h,w = to_visit.pop()

  dq = deque([(h,w)])
  reachable = set([(h,w)])
  blacks = 0
  whites = 0
  if S[h][w]==1:
    blacks += 1
  else:
    whites += 1

  while dq:
    h,w = dq.pop()
    nexts = [(h-1,w),(h+1,w),(h,w-1),(h,w+1)]
    for nxt in nexts:
      if nxt in reachable:
        continue
      else:
        if S[h][w] + S[nxt[0]][nxt[1]]==0:
          to_visit.remove(nxt)
          dq.append(nxt)
          reachable.add(nxt)
          if S[nxt[0]][nxt[1]]==1:
            blacks +=1
          else:
            whites +=1

  answer += blacks * whites
print(answer)