def actual(A, B, C):
    if A[-1] == B[0] and B[-1] == C[0]:
        return 'YES'

    return 'NO'

A, B, C = input().split()
print(actual(A, B, C))