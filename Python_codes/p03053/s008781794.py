from collections import deque
from sys import stdin
input = stdin.readline

INF = 1 << 21


def main():
  H, W = list(map(int, input().split()))
  M = [input()[:-1] for _ in range(H)]

  blacks = deque()
  whites = []
  d = [[INF]*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if M[i][j] == '#':
        blacks.append((i, j))
        d[i][j] = 0
      elif M[i][j] == '.':
        whites.append((i, j))

  def bfs(q, d):
    is_visited = [[0]*W for _ in range(H)]
    while len(q):
      ur, uc = q.popleft()
      d_ur = d[ur]
      for vr, vc in [(ur+1, uc), (ur-1, uc), (ur, uc-1), (ur, uc+1)]:
        if 0 <= vr < H and \
           0 <= vc < W:

          d_vr = d[vr]
          is_visited_vr = is_visited[vr]
          if not(is_visited_vr[vc]) and not(M[vr][vc] == '#') and \
             (d_vr[vc] > d_ur[uc] + 1):

            d_vr[vc] = d_ur[uc] + 1
            is_visited_vr[vc] = True
            q.append((vr, vc))
    return d_ur[uc]

  print(bfs(blacks, d))


if(__name__ == '__main__'):
  main()