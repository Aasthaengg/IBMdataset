from functools import reduce

N = int(input())
xors = list(map(int, input().split()))
all_xor = reduce(lambda a, b: a^b, xors)
for xor in xors:
  print(xor^all_xor)
