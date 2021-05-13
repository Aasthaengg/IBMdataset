#!/usr/bin/env python3

S = input()
T = input()

cnt = 0
while cnt < len(S):
    S = S[-1] + S[:-1]
    cnt += 1
    if S == T:
        print('Yes')
        exit()


print('No')
