import itertools
x = int(input())
itr = list(itertools.accumulate([i for i in range(100000)]))
for i in range(100000):
  if itr[i] < x <= itr[i + 1]:
    print(i + 1)
    exit()