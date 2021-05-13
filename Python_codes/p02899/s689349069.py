from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))

  order = []
  for i in range(N):
    order.append((i+1, A[i]))
  order = sorted(order, key=lambda x: x[1])
  for i in range(N-1):
    print(order[i][0], end=' ')
  print(order[N-1][0])


if(__name__ == '__main__'):
  main()
