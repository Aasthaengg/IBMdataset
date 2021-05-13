from math import gcd
N = int(input())
A = list(map(int,input().split()))
ans = A[0]

for e in A:
    ans = gcd(e,ans)
print(ans)