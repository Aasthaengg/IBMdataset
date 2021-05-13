from collections import deque
from sys import stdin
input = stdin.readline


def main():
  H, W = list(map(int, input().split()))
  M = [input()[:-1] for _ in range(H)]

  white = 0
  black = 0
  for i in range(H):
    for j in range(W):
      if M[i][j] == '.':
        white += 1
      elif M[i][j] == '#':
        black += 1

  start = (0, 0)
  q = deque()
  q.append(start)
  is_visited = [[0]*W for _ in range(H)]
  d = [[float('inf')]*W for _ in range(H)]
  d[0][0] = 0

  while len(q):

    ur, uc = q.popleft()

    for vr, vc in [(ur, uc+1), (ur, uc-1), (ur-1, uc), (ur+1, uc)]:
      if 0 <= vr < H and \
         0 <= vc < W and \
         not(is_visited[vr][vc]) and not(M[vr][vc] == '#'):

        q.append((vr, vc))
        is_visited[vr][vc] = True
        d[vr][vc] = d[ur][uc] + 1

  if d[H-1][W-1] == float('inf'):
    print(-1)
  else:
    print(white - (d[H-1][W-1] + 1))


if(__name__ == '__main__'):
  main()