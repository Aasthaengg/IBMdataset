from fractions import gcd
N=int(input())
A=[int(i) for i in input().split()]
ans=A[0]
for i in range(N-1):
    ans=gcd(ans,A[i+1])
print(ans)