import math
N = int(input())
prime = True
if N == 2:
  print(2)
  exit()
else:
  for k in range(N, 110000):
    prime = True
    max = math.ceil(math.sqrt(k))
    for i in range(2, max+1):
      if k % i == 0:
        prime = False
        break
    if prime == True:
      ans = k
      break
print(ans)