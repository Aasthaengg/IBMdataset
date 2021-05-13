S = str(input())
N = len(S)
for i in range(N-1):
    for j in range(i+1, N):
        tmp = S[:i+1] + S[j:]
        if tmp == 'keyence':
            print('YES')
            quit()

print('NO')