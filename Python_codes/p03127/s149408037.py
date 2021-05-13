N = int(input())
A = list(map(int, input().split()))

#最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd_calc = A[0]
for a in A[1:]:
    gcd_calc = gcd(gcd_calc, a)

print(gcd_calc)
