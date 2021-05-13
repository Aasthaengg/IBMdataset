a = [int(i) for i in input().split()]
A = a[0]
B = a[1]
K = a[2]

t = 0
while t < K:
    if A % 2 == 1:
        A -= 1
    A /= 2
    B += A
    t += 1

    if t < K:
        if B % 2 == 1:
            B -= 1
        B /= 2
        A += B
        t += 1

A = int(A)
B = int(B)

print(A,B)