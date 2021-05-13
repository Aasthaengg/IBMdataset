N = input()
A = list(map(int, input().split()))

l = sorted([ x - (idx+1) for x,idx in enumerate(A)])
#print(l)

import statistics
median = statistics.median(l)
#print(median)

ans = 0
for x in l:
  ans += abs(x - median)
  
print(int(ans))