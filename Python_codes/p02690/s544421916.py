from sys import stdin
input = stdin.readline


def main():
  X = int(input())

  for b in range(-500, 500):
    for a in range(-500, 500):
      if a**5 - b**5 == X:
        print(a, b)
        return


if(__name__ == '__main__'):
  main()
