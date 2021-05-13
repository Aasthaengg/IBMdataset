import string
from itertools import permutations

S = input()
if len(S) == 26:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    else:
        for i in range(25, -1, -1):
            j = 0
            while chr(ord(S[i]) + j + 1) <= "z":
                j += 1
                if chr(ord(S[i]) + j) not in set(S[:i]):
                    print(S[:i] + chr(ord(S[i]) + j))
                    exit()
else:
    for c in string.ascii_lowercase:
        if c not in S:
            print(S + c)
            exit()
