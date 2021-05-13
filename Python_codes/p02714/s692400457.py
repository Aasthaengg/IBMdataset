
import bisect
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  S = input()[:-1]

  R = []
  G = []
  B = []
  for i in range(N):
    if S[i] == 'R':
      R.append(i+1)
    elif S[i] == 'G':
      G.append(i+1)
    elif S[i] == 'B':
      B.append(i+1)

  Rset = set(R)
  Gset = set(G)
  Bset = set(B)

  sum_ = 0
  for ri in R:
    for gi in G:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(B, gi)
      if idx == len(B): continue
      sum_ += (len(B) - idx)
      if (2*gi - ri) in Bset:
        sum_ -= 1

  for ri in R:
    for gi in B:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(G, gi)
      if idx == len(G): continue
      sum_ += (len(G) - idx)
      if (2*gi - ri) in Gset:
        sum_ -= 1

  for ri in G:
    for gi in R:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(B, gi)
      if idx == len(B): continue
      sum_ += (len(B) - idx)
      if (2*gi - ri) in Bset:
        sum_ -= 1

  for ri in G:
    for gi in B:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(R, gi)
      if idx == len(R): continue
      sum_ += (len(R) - idx)
      if (2*gi - ri) in Rset:
        sum_ -= 1

  for ri in B:
    for gi in R:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(G, gi)
      if idx == len(G): continue
      sum_ += (len(G) - idx)
      if (2*gi - ri) in Gset:
        sum_ -= 1

  for ri in B:
    for gi in G:
      if ri >= gi:
        continue
      idx = bisect.bisect_right(R, gi)
      if idx == len(R): continue
      sum_ += (len(R) - idx)
      if (2*gi - ri) in Rset:
        sum_ -= 1

  print(sum_)


if(__name__ == '__main__'):
  main()
