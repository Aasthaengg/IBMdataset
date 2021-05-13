import sys
input = sys.stdin.readline
S = input()[: -1]
if len(S) == 3: print(S[: : -1])
else: print(S)