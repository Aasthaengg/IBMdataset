H,W = map(int, input().split())
s = [input() for _ in range(H)]

import sys
for j in range(1,H-1):
    for i in range(1,W-1):
        if s[j][i] =='#':
            if s[j][i-1] == '#':
                pass
            elif s[j-1][i] == '#':
                pass
            elif s[j][i+1] == '#':
                pass
            elif s[j+1][i] == '#':
                pass
            else:
                print('No')
                sys.exit()
print('Yes')
