#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A,B,C = inputlist()
if A+B>=C:
    print(B+C)
else:
    count = 0
    count = 2*B
    C -=B
    if C <= A+1:
        count +=C
    else:
        count += A+1
    print(count)