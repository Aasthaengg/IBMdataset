#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A,B = inputlist()
print(max(A+B,A-B,A*B))