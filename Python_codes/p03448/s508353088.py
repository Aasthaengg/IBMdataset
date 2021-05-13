# input
A = int(input())
B = int(input())
C = int(input())
X = int(input())

# check
if X % 100 == 50 and C == 0:
    print(0)
else:
    all_case = len(
        [
            1
            for a in range(A + 1)
            for b in range(B + 1)
            for c in range(C + 1)
            if 500 * a + 100 * b + 50 * c == X
        ]
    )

    print(all_case)