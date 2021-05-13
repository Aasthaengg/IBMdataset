from bisect import *
A = {1}
for p in range(2,11):
    for b in range(2,33):
        A.add(b**p)
A = list(A)
A.sort()
X = int(input())
print(A[bisect_right(A,X)-1])