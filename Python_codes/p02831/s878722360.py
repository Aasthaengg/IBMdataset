import math
import fractions
def lem(x,y):
	return (x * y) // fractions.gcd(x,y)

A,B = map(int, input().split())
print(lem(A,B))
