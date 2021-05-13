import math

def isinteger(n):
    if isinstance(n, int):
        return True
    elif isinstance(n,float):
        return n.is_integer()
    return False

n = int(input())
A = list(map(int,input().split()))
for i in range(1,n+1):
    A[i-1] = A[i-1]-i
A.sort()
if n % 2 == 1:
    b = A[(n-1)//2]
else:
    b = (A[n//2]+A[n//2]-1)/2
if isinteger(b):
    ans = 0
    for i in A:
        ans += abs(i-b)
    print(ans)
else:
    ans1=0
    ans2=0
    b1= math.floor(b)
    b2=b1+1
    for i in A:
        ans1 += abs(i-b1)
        ans2 += abs(i-b2)
    print(min(ans1,ans2))