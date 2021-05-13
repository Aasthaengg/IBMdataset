N = int(input())
S = input()
l = len(S)
S1 = S[:l//2]
S2 = S[l//2:]
if S1 == S2:
    print('Yes')
else:
    print('No')