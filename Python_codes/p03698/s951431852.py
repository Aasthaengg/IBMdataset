import sys
S = str(input())

from collections import Counter
for i in range(len(S)):
    if S.count(S[i]) > 1:
        print('no')
        sys.exit()
print('yes')