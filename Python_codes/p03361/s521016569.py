#!/usr/bin/env python

h, w = map(int, input().split())
s = ['' for _ in range(h+2)]
for i in range(1, h+1):
    s[i] = input()
for i in range(w):
    s[0] += '.' 
    s[h+1] += '.' 
for i in range(h+2):
    s[i] = ('.'+s[i]+'.')

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '#':
            if s[i][j-1] == '#' or s[i][j+1] == '#' or s[i-1][j] == '#' or s[i+1][j] == '#' :
                continue
            else:
                print('No')
                exit()
        else:
            continue

print('Yes')
