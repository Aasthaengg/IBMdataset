N, A, B = [int(x) for x in input().split()]

term = A + B
blue = (N // term) * A

if N - ((N // term) * term) <= A:
    blue += (N - ((N // term) * term))
else:
    blue += A

print(blue)
