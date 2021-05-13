from pprint import pprint as pp
import collections
import math
import itertools

K, = map(int, input().split())
A = tuple(map(int, input().split()))

old_a = A[-1]
x_max = 2 // A[-1]
x_min = 2 // A[-1]
for a in reversed(A):
  #pp((a, old_a, x_min, x_max))
  if a >= (old_a * (x_max +1)):
    x_max = -1
    break
  x_max = (old_a * (x_max+1)-1) // a
  x_min = math.ceil(old_a * x_min / a)
  if x_max < x_min:
    x_max = -1
    break
  old_a = a
#pp((old_a, x_min, x_max))
if x_max == -1:
  print(-1)
else:
  print(old_a * x_min, (old_a * (x_max+1))-1)
