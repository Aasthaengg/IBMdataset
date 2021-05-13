def remaining_balls():
    # 入力
    S, T = input().split()
    A, B = map(int, input().split())
    U    = input()
    # 処理
    if S == U:
        print(A-1, B)
    else:
        print(A, B-1)

remaining_balls()