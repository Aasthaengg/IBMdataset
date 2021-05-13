def actual(A, B, C, X):
    count = 0

    for n_500yen in range(A + 1):
        for n_100yen in range(B + 1):
            for n_050yen in range(C + 1):
                amount = 500 * n_500yen + 100 * n_100yen + 50 * n_050yen

                if amount == X:
                    count += 1

    return count

A = int(input())
B = int(input())
C = int(input())
X = int(input())

print(actual(A, B, C, X))
