A,B,C = list(map(int,input().split()))

if A == B and not A == C:
    print("Yes")
elif A == C and not A == B:
    print("Yes")
elif B == C and not B == A:
    print("Yes")
else:
    print("No")
