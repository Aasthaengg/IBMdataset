import numpy as np

N = int(input())
d = sorted(map(int, input().split()))

med = np.median(d)
if med in d:
  print(0)
  
else:
  lar = [x for x in d if x>med]
  sma = [x for x in d if x<med]

  print(lar[0]-sma[-1])