import bisect
import math

N = int(input())
As = list(map(int, input().split()))

As.sort()
a = As[-1]
j = bisect.bisect_left(As, a/2)

if j == 0 or a - As[j] > As[j-1]:
  print("{} {}".format(a, As[j]))
else:
  print("{} {}".format(a, As[j-1]))