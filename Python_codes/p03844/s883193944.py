def actual(A, op, B):
    if op == '+':
        return A + B

    return A - B

A, op, B = input().split()
A, B = int(A), int(B)

print(actual(A, op, B))