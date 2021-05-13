import math
from itertools import  accumulate
n = int(input())
tmp = n

sum = 0
a = 0
ans = []
for i in range(1,n+1):
    sum += i
    ans.append(i)
    if sum >= n:
        a = i
        break

d = sum - n
if d in ans:
    ans.remove(d)

for i in sorted(ans):
    print(i)