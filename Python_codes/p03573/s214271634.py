# ε₯ε
A, B, C = map(int, input().split())

# εΊε
if -100 <= A and B and C <= 100:
    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif A == C:
        print(B)