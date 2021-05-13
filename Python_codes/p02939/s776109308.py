# -*- coding: utf-8 -*-
s = input()

ans = 1
i = 2
tmp = s[0]
tmp2 = 1
while i <= len(s):
    if s[tmp2:i] != tmp:
        #print('a', i)
        tmp = s[tmp2:i]
        tmp2 = i
        ans += 1
        i += 1
    else:
        #print('b', i)
        i += 1
print(ans)
