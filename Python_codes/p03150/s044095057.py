S = input()
N = len(S)
res = 'NO'
for i in range(N + 1):
    for j in range(i, N + 1):
        if S[:i] + S[j:] == 'keyence':
            res = 'YES'
print(res)