A, B, C = map(int,input().split())
if A == B == C:
    print('No')
elif B == C:
    print('Yes')
elif A == C:
    print('Yes')
elif A == B:
    print('Yes')
else:
    print('No')