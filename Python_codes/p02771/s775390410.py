A, B, C = map(int, input().split())

if A == B == C or A != B != C != A:
    print("No")
else:
    print("Yes")