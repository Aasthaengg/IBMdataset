N, A, B, C, D = map(int, input().split())
S = 'x' + input()
mx = D if D > C else C
if '##' in S[A:mx]:
    print('No')
    exit()
if C > D:
    if '...' in S[B-1:D+2]:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
