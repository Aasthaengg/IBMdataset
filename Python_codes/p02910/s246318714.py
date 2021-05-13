S = input()
if not 'L' in S[::2] and not 'R' in S[1::2]:
    print('Yes')
else:
    print('No')
