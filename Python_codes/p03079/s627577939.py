A, B, C = map(int, input().split())
if A == B and B == C and C == A:
    print("Yes")
elif A!=B or B!=C or C!=A:
    print("No")