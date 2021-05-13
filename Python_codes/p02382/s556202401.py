import math

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = [abs(X-Y) for (X,Y) in zip(x, y)]

print(sum(z))

z2 = [Z ** 2 for Z in z]
z3 = [Z ** 3 for Z in z]

print(math.sqrt(sum(z2)))
print(math.pow(sum(z3),1/3))
print(max(z))