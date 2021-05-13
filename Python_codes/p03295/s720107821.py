from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  A_B = [list(map(int, input().split())) for _ in range(M)]

  A_B.sort(key=lambda x: x[1])

  added = [A_B[0][1]]
  for i in range(1, M):
    pre_b = added[-1]
    a, b = A_B[i]
    if pre_b <= a:
      added.append(b)

  print(len(added))


if(__name__ == '__main__'):
  main()