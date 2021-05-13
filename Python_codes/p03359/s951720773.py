#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
a,b = inputlist()
if a <= b:
    print(a)
else:
    print(a-1)