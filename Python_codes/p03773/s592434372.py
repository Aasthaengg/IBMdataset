def actual(A, B):
    return (A + B) % 24

A, B = map(int, input().split())
print(actual(A, B))