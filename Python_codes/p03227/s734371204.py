import sys

S = str(input())

moji = len(S)

if moji == 2:
    print(S)
elif moji == 3:
        print(S[2:3],end='')
        print(S[1:2],end='')
        print(S[0:1],end='')
