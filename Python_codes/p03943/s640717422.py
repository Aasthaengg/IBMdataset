import numpy as np

candy_packs = list(map(int, input().split(" ")))
to_be_candies = np.sum(candy_packs)/2

if to_be_candies in candy_packs:
  print("Yes")
else:
  print("No")