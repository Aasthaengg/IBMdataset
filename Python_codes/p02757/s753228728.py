import numpy as np

def a():
  n, p = list(map(int, input().split()))
  num = [int(s) for s in input()]
  
  if(p==2 or p==5):
    count=0
    for i in range(1,n+1):
      if(num[-i]%p == 0):
        count += n-i+1
    print(count)
    return
  
  counts = np.zeros(p)
  tmp = 0
  tens = 1
  for i in range(1,n+1):
    tmp = (tens*num[-i] + tmp) % p
    counts[tmp] += 1
    tens = (tens*10)%p
  ret = int(counts[0] + sum(counts*(counts-1)//2))
  print(ret)
  return
a()