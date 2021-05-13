import math
N = int(input())
count = 0

for i in range(N):
  n_size = int(math.log10(N-i)+1)
  if n_size%2==1:
    count += 1
  else:
    count += 0
  i += 1
print(count)