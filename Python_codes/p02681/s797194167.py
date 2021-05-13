import sys
S = input()
T = input()

if not ( S.islower() and T.islower() ): sys.exit()
if not ( 1 <= len(S) <= 10 and len(S) + 1 == len(T) ): sys.exit()

print('Yes') if S == T[:-1] else print('No')