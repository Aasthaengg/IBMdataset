def resolve():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]
    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    A[i][j] = None
                    break
    for i in range(3):
        for j in range(3):
            if A[i][j] is not None:
                break
        else:
            print("Yes")
            return
    for i in range(3):
        for j in range(3):
            if A[j][i] is not None:
                break
        else:
            print("Yes")
            return
    if all(map(lambda x: x is None, [A[0][0], A[1][1], A[2][2]])) or all(map(lambda x: x is None, [A[0][2], A[1][1], A[2][0]])):
        print("Yes")
        return
    print("No")


if '__main__' == __name__:
    resolve()