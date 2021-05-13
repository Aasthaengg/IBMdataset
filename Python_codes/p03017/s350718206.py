N, A, B, C, D = map(int, input().split())
S = input()

if C > D:
    ai = A - 1
    bi = B - 1
    while ai < C - 1:
        if ai + 1 < C and S[ai + 1] == '.' and ai + 1 != bi:
            ai += 1
        else:
            if ai + 2 < C and S[ai + 2] == '.' and ai + 2 != bi:
                ai += 2
            else:
                if bi + 1 < D and S[bi + 1] == '.':
                    bi += 1
                elif bi + 2 < D and S[bi + 2] == '.':
                    bi += 2
                else:
                    print('No')
                    exit()
    while bi < D - 1:
        if S[bi + 1] == '.':
            bi += 1
        else:
            if bi + 2 < D and S[bi + 2] == '.':
                bi += 2
            else:
                print('No')
                exit()

else:
    bi = B - 1
    while bi < D - 1:
        if S[bi + 1] == '.':
            bi += 1
        else:
            if bi + 2 < D and S[bi + 2] == '.':
                bi += 2
            else:
                print('No')
                exit()

    ai = A - 1
    while ai < C - 1:
        if S[ai + 1] == '.':
            ai += 1
        else:
            if ai + 2 < C and S[ai + 2] == '.':
                ai += 2
            else:
                print('No')
                exit()

print('Yes')
