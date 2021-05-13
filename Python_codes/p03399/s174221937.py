#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(min(A,B) + min(C,D))