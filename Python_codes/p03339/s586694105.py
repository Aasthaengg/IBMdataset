from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = input()[:-1]

  E = [0]
  for a in A:
    if a == 'E':
      E.append(E[-1]+1)
    else:
      E.append(E[-1])

  min_ = float('inf')
  for i in range(N):
    min_ = min(min_, (i-E[i])+(E[N]-E[i+1]))
  print(min_)


if(__name__ == '__main__'):
  main()