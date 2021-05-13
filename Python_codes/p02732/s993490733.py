from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))

  dic = defaultdict(int)
  for a in A:
    dic[a] += 1

  C2 = lambda N: int(N * (N-1) / 2)

  sum_ = 0
  for key in dic.keys():
    sum_ += C2(dic[key])

  for i in range(N):
    print( sum_ - (C2(dic[A[i]]) - C2(dic[A[i]]-1)) )


if(__name__ == '__main__'):
  main()
