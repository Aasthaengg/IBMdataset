import sys

input = sys.stdin.readline


def main():
  N, M = map(int, input().strip().split())
  S = input().strip()
  
  print(S[:M-1] + S[M-1].lower() + S[M:])


if __name__ == '__main__':
  main()
