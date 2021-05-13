# 解説確認後

import fractions #val 3.4

N = int(input())

a = list(map(int,input().split()))

gcd = fractions.gcd(a[0],a[1])

for i in range(2,N):
    gcd = fractions.gcd(a[i],gcd)
print(gcd)