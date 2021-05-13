import sys
from collections import defaultdict
from collections import deque
from sys import stdin
sys.setrecursionlimit(10**7)
input = stdin.readline


def main():
  # input
  N, Q = list(map(int, input().split()))

  G = [[] for _ in range(N+1)]
  for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

  PX = defaultdict(int)
  for _ in range(Q):
    p, x = map(int, input().split())
    PX[p] += x

  # solve
  ans = [0]*(N+1)
  visited = set()
  # temp = PX[1]
  # S = [1] # Stack
  # S = deque([1])

  # while len(S):
  #   now = S[-1]
  #   visited.add(now)

  #   for next_ in G[now]:
  #     if next_ not in visited:
  #       S.append(next_)
  #       temp += PX[next_]
  #       break
  #   else:
  #     S.pop()
  #     ans[now] = temp
  #     temp -= PX[now]

  def dfs(now, sum_):
    visited.add(now)
    for next_ in G[now]:
      if next_ not in visited:
        sum_ += PX[next_]
        sum_ = dfs(next_, sum_)

    ans[now] = sum_
    sum_ -= PX[now]
    return sum_

  dfs(1, PX[1])

  print(*ans[1:], sep=' ')


if(__name__ == '__main__'):
  main()
