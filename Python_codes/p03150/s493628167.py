S = input()

import sys

for i in range(0,len(S)):
    for j in range(i,len(S)):
        if S[:i] + S[j:] == 'keyence':
            print('YES')
            sys.exit()
        
print('NO')