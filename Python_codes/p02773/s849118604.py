from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  dic = defaultdict(int)
  for i in range(N):
    dic[input()[:-1]] += 1

  max_ = max(dic.values())
  out = []
  for key, val in dic.items():
    if val == max_:
      out.append(key)

  print(*sorted(out), sep='\n')


if(__name__ == '__main__'):
  main()
