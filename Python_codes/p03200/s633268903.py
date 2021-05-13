from sys import stdin
input = stdin.readline


def main():
  S = input()[:-1]

  cnt = 0
  nw = 0
  for i, s in enumerate(S):
    if s == 'W':
      cnt += (i-nw)
      nw += 1

  print(cnt)


if(__name__ == '__main__'):
  main()
