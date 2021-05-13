n=int(input())
a=list(map(int,input().split()))
import fractions
def gcdlist(a):
    ans = a[0]
    for i in range(1, len(a)):
        ans = fractions.gcd(ans, a[i])
    return ans
print(gcdlist(a))