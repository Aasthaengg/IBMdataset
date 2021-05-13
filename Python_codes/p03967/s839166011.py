# -*- coding: utf-8 -*-
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

s = list(input())
g = 0
p = 0
ans = 0
for i in range(len(s)):
    if s[i] == 'g' and p + 1 <= g:
        ans += 1
        p += 1
        #print('a')
    elif s[i] == 'g' and p <= g + 1:
        g += 1
        #print('b')
    elif s[i] == 'p' and p + 1 <= g:
        p += 1
        #print('d')
    elif s[i] == 'p' and p <= g + 1:
        ans -= 1
        g += 1
        #print('c')
print(ans)
