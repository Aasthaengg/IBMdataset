def resolve():
    # 整数 1 つ
    n = int(input())
    # 整数複数個
    # a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    result = 0
    while len(A) > 1:
        flag = False
        for i in range(1, len(A)):
            if A[0] == A[i]:
                continue
            elif A[0] < A[i]:
                j = i
                while A[j-1] <= A[j]:
                    j += 1
                    if j == len(A):
                        A = []
                        result += 1
                        flag = True
                        break
                else:
                    del A[:j]
                    result += 1
                    flag = True
            elif A[0] > A[i]:
                j = i
                while A[j-1] >= A[j]:
                    j += 1
                    if j == len(A):
                        A = []
                        result += 1
                        flag = True
                        break
                else:
                    del A[:j]
                    result += 1
                    flag = True
            if flag == True:
                break
    else:
        if len(A) == 1:
            result += 1
    print(result)

resolve()