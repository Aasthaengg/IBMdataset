import fractions
from functools import reduce

N,K = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse = True)

def gcd_list(numbers):
  return reduce(fractions.gcd, numbers)

GCD = gcd_list(A)

if K > A[0]:
  print("IMPOSSIBLE")
elif K % GCD != 0:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")