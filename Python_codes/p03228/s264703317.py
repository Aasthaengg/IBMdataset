A, B, K = [int(i) for i in input().split()]

for i in range(0, K):

    if (i % 2 == 0):

        if (A % 2 != 0):
            A = A - 1

        a = A / 2
        A -= a
        B += a
    else:

        if (B % 2 != 0):
            B = B - 1

        b = B / 2
        B -= b
        A += b

print(int(A), int(B))