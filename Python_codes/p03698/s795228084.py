import sys
S = str(input())
if len(S) < 2 or len(S) > 27:
    sys.exit()
if not S.islower():
    sys.exit()

result = 'yes'
for I in range(len(S)):
    if S.count(S[I]) > 1:
        result = 'no'
print(result)