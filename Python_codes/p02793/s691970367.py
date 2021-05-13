import sys
sys.setrecursionlimit(4100000)
import math




N = int(input())


import fractions
a = list(map(int, input().split()))
koubai = a[0]
small = []
for i in range(0, N//2):
    small.append(a[2*i + 1] * a[2*i] // fractions.gcd(a[2*i + 1], a[2*i]))

small.append(a[-1])
for i in range(len(small)):
    koubai = koubai * small[i] // fractions.gcd(koubai, small[i])


ans = int(0)
for i in range(N):
    ans += koubai // a[i]
    
ans %= 1000000007

print(ans)