from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))

  dic = defaultdict(int)
  for i, a in enumerate(A):
    dic[a] += 1

  for i in range(1, N+1):
    print(dic[i])


if(__name__ == '__main__'):
  main()
