N, A, B = map(int, input().split())

maximum = min([A, B])

if A+B >= N:
    minimum = (A+B) - N
else:
    minimum = 0

print(maximum, minimum)
