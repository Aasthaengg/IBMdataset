def actual(A, B):
    sum_ = A + B

    if sum_ < 10:
        return sum_

    return 'error'

A, B = map(int, input().split())
print(actual(A, B))