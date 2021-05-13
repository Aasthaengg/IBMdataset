import math

A, B, N = map(int, input().split())

if B > N:
    x = N
elif B == N:
    x = N - 1
else:
    x = B -1

answer = math.floor(A * x / B) - A * math.floor( x / B)

print(answer)