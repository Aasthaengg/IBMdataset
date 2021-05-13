from sys import stdin
input = stdin.readline


def check(min_, max_, x):
  ret = sum([10**gap for gap in range(len(str(x))-2)])
  if min_ <= x:
    ret += int((min(max_, x) - min_)/10) + 1
  return ret


def main():
  N = int(input())

  if len(str(N)) == 1:
    print(N)
    return
  sum_ = 0
  for l in range(1, 10):
    for r in range(l, 10):
      min_ = int(str(l) + '0'*(len(str(N))-2) + str(r))
      max_ = int(str(l) + '9'*(len(str(N))-2) + str(r))
      A = check(min_, max_, N)

      min_ = int(str(r) + '0'*(len(str(N))-2) + str(l))
      max_ = int(str(r) + '9'*(len(str(N))-2) + str(l))
      B = check(min_, max_, N)

      if l == r:
        A += 1
        B += 1
        sum_ += A*B
      else:
        sum_ += 2*A*B

  print(sum_)


if(__name__ == '__main__'):
  main()
