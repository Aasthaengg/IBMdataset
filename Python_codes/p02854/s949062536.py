import numpy as np

n = int(input())
a = list(map(int, input().split()))

cum = np.cumsum(a)
mid = cum[-1]/2
diff = 10**10
for each in cum:
  diff = min(diff, abs(mid-each))
  
print(int(diff/0.5))