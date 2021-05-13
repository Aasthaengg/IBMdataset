#template
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
A = inputlist()
c = Counter(A)
key = c.keys()
count = 0
for i in key:
    count += c[i]-1
l = len(set(A))
if count % 2 == 1:
    l-=1
print(l)