from collections import Counter

def SUMCHK():
    N = int(input())
    S = input()

    C=Counter(S)
    r = C['R']
    g = C['G']
    b = C['B']


    cnt = r * g * b

    for i in range(0,N-2):
        for j in range(i,N-1):
            k = j + j - i
            if k < N:
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                    cnt -= 1

    print(cnt)

SUMCHK()
