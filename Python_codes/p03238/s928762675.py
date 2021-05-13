#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める

N = int(input())
if N == 1:
    print("Hello World")
if N == 2:
    A = int(input())
    B = int(input())
    print(A+B)