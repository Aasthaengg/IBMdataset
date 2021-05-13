n = int(input())
import fractions
A = list(map(int,input().split()))
g = 0
for i in range(n):
    g = fractions.gcd(g,A[i])
print(g)
