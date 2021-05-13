def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    n, a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    # turn = A
    # while not ((a == 1 and b == 2) or (a == (n-1) and b == n)):
    #     if turn == A:
    #         if a + 1 < b:
    #             a += 1
    #         else:
    #             a -= 1
    #         turn = B
    #     else:
    #         if a + 1 < b:
    #             b -= 1
    #         else:
    #             b += 1
    #         turn = A

    if (b - a) % 2 == 1:
        print("Borys")
    else:
        print("Alice")


#    print("n")


resolve()