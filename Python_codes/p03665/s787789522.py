def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
import math

n,p = iim()
A = iil()

if n > 1:
    even = 0
    odd = 0
    for i in A:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    if odd > 0:
        p0 = 2**(odd-1)
        print(2**even*p0)
    else:
        print(2**even if p == 0 else 0)
else:
    if p == 0:
        print(2 if A[0]%2 == p else 0)
    else:
        print(1 if A[0]%2 == p else 0)
