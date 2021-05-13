import sys
N = int(input())
S = input()
unique_S = list(set(list(S)))

sys.exit() if not (2 <= N <= 100) else ''
sys.exit() if len(S) != N else ''
sys.exit() if not S.islower() else ''

result = 0
for I in range(len(S)):
    count = 0
    for J in range(len(unique_S)):
        if ( unique_S[J] in S[0:I] ) and ( unique_S[J] in S[I:] ):
            count += 1
        if result < count:
            result = count

print(result)