from collections import Counter
for key, nums in Counter(list(map(int,input().split()))).items():
  if nums == 1: print(key)