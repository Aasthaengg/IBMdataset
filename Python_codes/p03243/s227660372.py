#!/usr/bin/env python3


S = input()

if int(S[0]) >= int(S[1]) and int(S[0]) >= int(S[2]):
    print(S[0]*3)
else:
    print(str(int(S[0])+1)*3)
