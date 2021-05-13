a =int(input())
l = list(map(int,input().split()))
l.sort()
import numpy as np
times = 1
for i in l:
  times*=i
  if times>10**18:
    times = -1
    break
print(times)