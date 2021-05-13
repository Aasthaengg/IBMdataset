A,B,C = map(int,input().split())

if A == B and A != C and B != C:
    print("Yes")
elif A == C and A != B and C != B:
    print("Yes")
elif B == C and B != A and C != A:
    print("Yes")
else:
    print("No")