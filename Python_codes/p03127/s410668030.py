import math

N = int(input())
A = list(map(int, input().split()))
g = [math.gcd(A[0], A[1])]
for i in range(2, N):
    g.append(math.gcd(g[-1], A[i]))
print(g[-1])
