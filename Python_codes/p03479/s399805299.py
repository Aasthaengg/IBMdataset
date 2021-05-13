from sys import stdin
input = stdin.readline


def main():
  X, Y = list(map(int, input().split()))
  cnt = 1
  while True:
    X *= 2
    if X > Y:
      break
    cnt += 1

  print(cnt)


if(__name__ == '__main__'):
  main()