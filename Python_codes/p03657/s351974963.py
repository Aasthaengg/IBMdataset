def actual(A, B):
    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        return 'Possible'

    return 'Impossible'

A, B = map(int, input().split())
print(actual(A, B))