#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
S = list(input())
if len(S) == 2:
    print(''.join(S))
else:
    print(''.join(reversed(S)))