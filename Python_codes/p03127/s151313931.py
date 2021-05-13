def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from fractions import gcd
n = ii()
A = iil()
cd = A[0]
for item in A:
    cd = gcd(cd,item)
print(cd)