A, B, C = map(int, input().split())

if A == B and B == C:
    print(1)
elif A == B or B == C or C == A:
    print(2)
else:
    print(3)