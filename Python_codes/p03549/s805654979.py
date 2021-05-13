#template
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#template
N,M = inputlist()
time = (N-M)*100*(2**M) + 1900*M*(2**M)
print(time)