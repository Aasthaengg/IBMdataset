import itertools
from sys import stdin
input = stdin.readline


def main():
  N, M, Q = list(map(int, input().split()))
  cands = itertools.combinations(range(N+M-1), N)
  Qs = [tuple(map(int, input().split())) for _ in range(Q)]

  seq = [0]*N
  max_ = 0
  for cand in cands:
    temp_max = 0
    for i in range(N):
      seq[i] = cand[i] - i

    for a, b, c, d in Qs:
      if seq[b-1] - seq[a-1] == c:
        temp_max += d
    max_ = max(max_, temp_max)

  print(max_)


if(__name__ == '__main__'):
  main()
