import numpy as np

n = int(input())
p = list(map(int,input().split(" ")))

def check_condition(l):
  if (l[0] < l[1] < l[2]) or  (l[0] > l[1] > l[2]):
    return 1
  else:
  	return 0

is_satisfied = [check_condition(p[i:i+3]) for i in range(n-2)]
  
print(np.sum(is_satisfied))