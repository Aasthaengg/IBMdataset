n = int(input())
A = list(map(int, input().split()))

A.sort()
from itertools import accumulate
C = [0]+A
C = list(accumulate(C))

def is_ok(x):
    if x == n-1:
        return True
    y = C[x+1]
    flag = True
    for i in range(x+1, n):
        if A[i] > 2*y:
            flag = False
        y += A[i]
    if flag:
        return True
    else:
        return False

if is_ok(0):
    print(n)
    exit()

l = 0
r = n-1
while l+1 < r:
    c = (l+r)//2
    if is_ok(c):
        r = c
    else:
        l = c
print(n-r)
