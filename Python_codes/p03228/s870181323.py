#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
A,B,K = inputlist()
count = 0
while True:
    if A % 2 == 1:
        A -=1
    d = A//2
    B += d
    A -=d
    count +=1
    if count == K:
        break
    if B % 2 == 1:
        B-=1
    da = B//2
    A += da
    B -=da
    count +=1
    if count == K:
        break
print(A,B)