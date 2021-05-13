# -*- coding: utf-8 -*-

S = list(str(input()))

while len(S) > 1:
    S.pop()
    if S[0 : len(S) // 2] == S[len(S) // 2 :] and len(S) % 2 == 0:
        print(len(S))
        exit()