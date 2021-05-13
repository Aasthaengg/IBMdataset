import fractions

N = int(input())
a, *A = map(int, input().split())

for x in A:
    a = fractions.gcd(x, a)

print(a)