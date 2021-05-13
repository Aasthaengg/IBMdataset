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
    if S[:len(K[i][0])] == K[i][0] and S[len(S)-len(K[i][1]):] == K[i][1]:
        print('YES')
        exit()
print('NO')


