# -*- coding: utf-8 -*-
import copy
s = list(input())

if ''.join(s) == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(s) == 26:
    for i in reversed(range(0, 26)):
        #for j in range(1, ord('z') - ord(s[i])):
        for j in range(ord(s[i]) + 1, ord('z') + 1):
            if not chr(j) in s[:i]:
                s[i] = chr(j)
                print(''.join(s[:i + 1]))
                exit()

for i in range(26):
    if not chr(ord('a') + i) in s:
        s.append(chr(ord('a') + i))
        break
ans2 = ''.join(s)
print(ans2)
