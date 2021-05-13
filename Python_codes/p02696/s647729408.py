from math import floor

A, B, N = map(int, input().split())

if N // B >= 1:
    if B != 1:
        x = B - 1
    else:
        x = 1
else:
    x = N

#print(x)
result = floor(A * x // B) - A * floor(x / B)

print(result)