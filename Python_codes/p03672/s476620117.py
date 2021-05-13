from sys import stdin
input = stdin.readline


def main():
  S = input()[:-1]

  dl = 2
  while dl < len(S):
    center = (len(S) - dl) // 2
    if S[:center] == S[center:-dl]:
      print(len(S)-dl)
      return
    dl += 2


if(__name__ == '__main__'):
  main()
