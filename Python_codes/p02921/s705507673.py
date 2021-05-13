import sys
S = input()
T = input()

if not ( len(S) == 3 and len(T) == 3 ): sys.exit()
if not ( ('S' in S or 'C' in S or 'R' in S) and ('S' in T or 'C' in T or 'R' in T)):
    sys.exit()

count = 0
for s in range(len(S)):
    if S[s] == T[s]: count += 1

print(count)