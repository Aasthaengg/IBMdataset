#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A,B = inputlist()
if A > 8 or B > 8:
    print(":(")
else:
    print("Yay!")