import sys
S = list(input())
if len(S) != 3:
    sys.exit()

print(S.count('o') * 100 + 700)