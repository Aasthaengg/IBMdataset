import sys
S = input()

min = 1000
for I in range(len(S)):
    if min > abs(753 - int(S[I:I+3])):
        min = abs(753 - int(S[I:I+3]))
print(min)