import sys
S = list(input())
if len(S) != 3:
    sys.exit


if S.count('a') == 1 and S.count('b') == 1 and S.count('c') == 1:
    print('Yes')
else:
    print('No')