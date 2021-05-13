import sys
S=input()
T=input()

for i in range(len(S)):
    S=S[-1]+S[:-1]
    if T==S:
        print('Yes')
        sys.exit()

print('No')