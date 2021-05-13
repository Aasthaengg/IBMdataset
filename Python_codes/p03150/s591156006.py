T = 'keyence'
S = input()

n = len(S) - len(T)

j = 0
for i in range(7):
    if T[i] == S[i]:
        continue
    else:
        j = i
        break

print('YES' if T == S[:j]+S[j+n:] else 'NO')