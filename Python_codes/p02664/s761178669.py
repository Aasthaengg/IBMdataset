S = list(input().strip())
n = len(S)
for i in range(n):
    if S[i] == '?':
        S[i] = 'D'
print(''.join(S))