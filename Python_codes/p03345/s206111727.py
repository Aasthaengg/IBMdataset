from sys import exit

A, B, C, K = map(int, input().split())


if A == B:
    print(0)
    exit()

if abs(A - B) > 10 ** 18:
    print("Unfair")
    exit()

sign = (A - B) // abs(A - B)


if K % 2 == 0:
    print(abs(A - B) * sign)
else:
    print(abs(A - B) * sign * (-1))
