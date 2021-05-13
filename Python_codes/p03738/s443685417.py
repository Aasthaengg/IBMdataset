def actual(A, B):
    if A > B:
        return 'GREATER'

    if A < B:
        return 'LESS'

    return 'EQUAL'


A = int(input())
B = int(input())

print(actual(A, B))
