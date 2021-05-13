import itertools
import numpy as np
import math

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

if p == q:
  print(0)
  exit()

lis = [x+1 for x in range(n)]

p_list = itertools.permutations(lis)

a, b = 0, 0
f_a, f_b = False, False
i = 0

for one_case in p_list:
  if list(one_case) == p:
    a = i
    i += 1
    f_a = True
  elif list(one_case) == q:
    b = i
    i += 1
    f_b = True
  else:
    i += 1
  if f_a and f_b:
    break
print(abs(a-b))