from sys import stdin
input = stdin.readline


def main():
  N, M, X = list(map(int, input().split()))
  C = []
  A = [[0]*M for _ in range(N)]

  for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A[i] = a

  min_ = float('inf')
  for bit in range(1 << N):
    temp = [0]*M
    cost = 0
    for i in range(N):
      mask = 1 << i
      if bit & mask:
        cost += C[i]
        for j, a in enumerate(A[i]):
          temp[j] += a

    if all(list(map(lambda x: x >= X, temp))):
      min_ = min(min_, cost)

  if min_ == float('inf'):
    print(-1)
  else:
    print(min_)


if(__name__ == '__main__'):
  main()
