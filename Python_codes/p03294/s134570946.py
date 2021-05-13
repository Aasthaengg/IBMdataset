from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input())
A = list(map(int,input().split()))

l = lcm(A[0], A[1])
for i in range(2,n):
    l = lcm(l, A[i])

ans = 0
for a in A:
    ans += (l-1)%a
    
print(ans)