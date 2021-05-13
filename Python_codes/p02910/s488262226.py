S = input()

if S[0::2].count('L') == 0 and S[1::2].count('R') == 0:
    print('Yes')
else:
    print('No')
