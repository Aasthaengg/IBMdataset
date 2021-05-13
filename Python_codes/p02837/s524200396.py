from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = [[-1]*N for _ in range(N)]
  for i in range(N):
    num = int(input())
    for _ in range(num):
      x, y = map(int, input().split())
      A[i][x-1] = y

  max_ = 0
  for bit in range(1 << N):
    for i in range(N):
      mask = (1 << i)
      # i番目の仮定についてN人の証言について検証
      for j in range(N):
        if A[j][i] == -1:
          continue
        # j番目の人が正直者と仮定してiについての証言が仮定と一致しない
        if (bit & (1 << j)) and A[j][i] != bool(bit & mask):
          # print(f'bit:{bin(bit)}, i:{i}, j:{j}, A[j][i]:{A[j][i]} != {bit & mask}')
          break
      else:
        # cnt += 1
        continue
      break
    else:
      # print(bin(bit))
      max_ = max(max_, bin(bit).count('1'))

  print(max_)


if(__name__ == '__main__'):
  main()
