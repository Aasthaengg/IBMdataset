S = input().split()
A, B, C = int(S[0]), int(S[1]), int(S[2])
if A + B < C:
    print('No')
else:
    print('Yes')