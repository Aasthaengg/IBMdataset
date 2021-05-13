A,B,C = input().split()
if A == B and A != C:
    print("Yes")
elif A == C and A != B:
    print("Yes")
elif B == C and A != B:
    print("Yes")
else:
    print("No")