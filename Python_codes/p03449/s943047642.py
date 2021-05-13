from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  U = list(map(int, input().split()))
  L = list(map(int, input().split()))

  SU = [0]
  for u in U:
    SU.append(u + SU[-1])

  SL = [0]
  for l in L:
    SL.append(l + SL[-1])

  max_ = 0
  for i in range(N):
    max_ = max(max_, SU[i+1]+SL[N]-SL[i])
  print(max_)


if(__name__ == '__main__'):
  main()