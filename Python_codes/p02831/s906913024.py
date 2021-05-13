A, B = map(int, input().split())
import fractions
C = fractions.gcd(A, B)
D = A * B / C
print(int(D))