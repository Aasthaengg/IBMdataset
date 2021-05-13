#!/usr/bin/env python3

S = input()
key = 'keyence'
K = []

if key in S:
    print('YES')
    exit()


for i in range(len(key)+1):
    K.append([key[:i],key[i:]])

for i in range(len(K)):
    if K[i][0] in S and K[i][1] in S:
        if S[0] == 'k' and S[-1] == 'e':
            print('YES')
            exit()
print('NO')


