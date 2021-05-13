from sys import stdin
input = stdin.readline


def main():
  A, B = list(map(int, input().split()))

  for i in range(10000):
    if int(i * 0.08) == A and \
       int(i * 0.10) == B:

      print(i)
      return
  print(-1)


if(__name__ == '__main__'):
  main()
