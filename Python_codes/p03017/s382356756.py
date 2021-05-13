def resolve():
    N, A, B, C, D = map(int, input().split())
    S = str(input())
    if C < D:
        if '##' in S[min(A, B):D]:
            print('No')
        else:
            print('Yes')
    elif C > D:
        if '##' in S[min(A, B):C]:
            print('No')
        else:
            if '...' in S[B-2:D+1]:
                print('Yes')
            else:
                print('No')


resolve()