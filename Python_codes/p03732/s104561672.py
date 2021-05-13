N, WW = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(N)]
W, V = zip(*l)
M = [{} for i in range(N + 1)]
def cal(i, w):
  if w in M[i]:
    return M[i][w]
  if i == N:
    v = 0
  elif w < W[i]:
    v = cal(i + 1, w)
  else:
    v = max(cal(i + 1, w), cal(i + 1, w - W[i]) + V[i])
  M[i][w] = v
  return v

print(cal(0, WW))