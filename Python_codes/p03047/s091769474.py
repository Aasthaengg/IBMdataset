#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
N,K = inputlist()
print(N-K+1)