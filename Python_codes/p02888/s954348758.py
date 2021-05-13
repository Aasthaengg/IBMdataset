from collections import defaultdict
import bisect
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  L = list(map(int, input().split()))

  # dic = defaultdict(int)
  # for l in L:
  #   dic[l] += 1
  # uniq = sorted(dic.keys())
  # sum_ = [0]*(uniq[-1]+1)
  # for i in range(1, uniq[-1]+1):
  #   sum_[i] = sum_[i-1] + dic[i]
  L = sorted(L)

  ans = 0
  for i in range(N):
    for j in range(i+1, N):
      if i == j:
        continue
      a = L[i]
      b = L[j]
      # lower = bisect.bisect_right(L[:i]+L[i+1:j]+L[j+1:], abs(a-b)) - 1
      # upper = bisect.bisect_right(L[:i]+L[i+1:j]+L[j+1:], a+b) - 1
      lower = bisect.bisect_right(L, abs(a-b), lo=j+1, hi=len(L)) - 1 - (j+1)
      upper = bisect.bisect_left(L, a+b, lo=j+1, hi=len(L)) - 1 - (j+1)
      # lower = bisect.bisect_right(L[j+1:], abs(a-b)) - 1
      # upper = bisect.bisect_left(L[j+1:], a+b) - 1

      # print(a, b, lower, upper)
      # print(f'--> {L[j+1:]}')

      # if lower < 0 or upper < 0: continue
      if upper < 0: continue
      ans += (upper - max(lower, 0) + 1)

  # print(dic)
  # print(uniq)
  # print(sum_)
  print(ans)


if(__name__ == '__main__'):
  main()
