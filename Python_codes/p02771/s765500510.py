A,B,C = map(int,input().split())
if A == B and B == C:
    print('No')
    exit()
if A != B and B != C and C != A:
    print('No')
    exit()
print('Yes')