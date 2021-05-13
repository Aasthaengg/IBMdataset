#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
H=int(input())
W = int(input())
N = int(input())
m = max(H,W)
n=N/m
if n.is_integer():
    print(int(n))
    exit()
else:
    print(int(n)+1)