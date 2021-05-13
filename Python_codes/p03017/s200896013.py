# -*- coding: utf-8 -*-
N, A, B, C, D = map(int, input().split(' '))
A -= 1
B -= 1
C -= 1
D -= 1


S = input()
if S[A:C+1].count('##') or S[B:D+1].count('##'):
    print('No')
    exit(0)

if C > D:
    if not S[B-1: D+2].count('...'):
        print('No')
        exit(0)

print('Yes')
















