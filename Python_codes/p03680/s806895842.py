from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = [int(input()) for _ in range(N)]

  set_ = set()
  set_.add(0)
  cur = 0
  next_ = 0
  cnt = 0

  while True:
    # push
    cnt += 1
    cur = next_
    next_ = A[cur] - 1
    if next_ == 1:
      print(cnt)
      break
    if next_ in set_:
      print(-1)
      break
    set_.add(next_)


if(__name__ == '__main__'):
  main()