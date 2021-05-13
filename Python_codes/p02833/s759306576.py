import sys
import math

N = int(input())
# N, K = [int(i) for i in input().split()]
if N == 0:
    print(0)
    sys.exit(0)
if N % 2 == 1:
    print(0)
    sys.exit(0)

count = 0
digit = math.ceil(math.log(N, 5))
for i in range(1, digit+1):
    x = 5 ** i
    count += (N // (x * 2))
print(count)
