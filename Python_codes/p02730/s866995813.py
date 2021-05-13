S = str(input())
if len(S) % 4 == 1:
    m = len(S) // 4
    for i in range(m):
        if (S[i] != S[2 * m - i - 1] or
            S[2 * m - i - 1] != S[2 * m + 1 + i] or
            S[2 * m + 1 + i] != S[4 * m - i]):
            print('No')
            exit()    
else:
    m = len(S) // 4 + 1
    for i in range(m - 1):
        if (S[i] != S[2 * m - i - 2] or
            S[2 * m - i - 2] != S[2 * m + i] or
            S[2 * m + i] != S[4 * m - i - 2]):
            print('No')
            exit()
    if S[m - 1] != S[3 * m - 1]:
        print('No')
        exit()
print('Yes')