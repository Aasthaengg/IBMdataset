import math

N = int(input())
A = list(map(int, input().split()))

# num is numerator
# den is denominator
num, den = A[0], 0

for i in A:
    num = (num * i) // math.gcd(num, i)

for i in A:
    den += num // i

ans = num / den
print(ans)
