def actual(A, B, C):
    if A <= C <= B:
        return 'Yes'

    return 'No'

A, B, C = map(int, input().split())
print(actual(A, B, C))