def solve():
    Ass = [tuple(map(int, input().split())) for _ in range(3)]
    N = int(input())
    Bs = set([int(input()) for _ in range(N)])

    isOKss = [[0]*(3) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if Ass[i][j] in Bs:
                isOKss[i][j] = 1

    for i in range(3):
        for j in range(3):
            if not isOKss[i][j]:
                break
        else:
            return True

    for j in range(3):
        for i in range(3):
            if not isOKss[i][j]:
                break
        else:
            return True

    for i in range(3):
        if not isOKss[i][i]:
            break
    else:
        return True

    for i in range(3):
        if not isOKss[i][2-i]:
            break
    else:
        return True

    return False


if solve():
    print('Yes')
else:
    print('No')
