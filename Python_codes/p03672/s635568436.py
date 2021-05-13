import sys
S = str(input())

if len(S) < 2 or len(S) > 200:
    sys.exit()
if not S.islower():
    sys.exit()

result = 0
for I in range(len(S)):
    length = len(S) - I
    if (not I == 0) and length % 2 == 0 and S[0:int(length / 2)] == S[int(length / 2):length]:
        print(length)
        sys.exit()