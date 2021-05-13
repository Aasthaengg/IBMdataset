#template
from collections import Counter
def inputlist(): return [int(k) for k in input().split()]
#template
N = int(input())
print(N*(N-1)//2)