import sys
S = list(input())

if len(S) != 4:
    sys.exit()

result = 0
for I in range(len(S)):
    if S[I] == '+':
        result += 1
    else:
        result -= 1

print(result)