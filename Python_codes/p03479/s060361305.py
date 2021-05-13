import sys


def resolve():
    readline = sys.stdin.readline    # 1行だけ文字列にする

    X, Y = map(int, readline().split())

    # Ai+1 = 2Aiとすればおｋ？
    A = X
    cnt = 1
    while 1:
        A = 2 * A
        if A <= Y:
            cnt += 1
        else:
            print(cnt)
            break


resolve()