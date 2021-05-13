import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    S = in_s() + "T"
    N = len(S)

    X, Y = in_nn()

    x_num = []
    y_num = []

    f = False
    first = True

    cnt = 0
    for i in range(N):
        if S[i] == "T":

            if cnt > 0:
                if f:
                    if first:
                        Y -= cnt
                    else:
                        y_num.append(cnt)
                else:
                    if first:
                        X -= cnt
                    else:
                        x_num.append(cnt)
            cnt = 0
            f = not f
            first = False
        else:
            cnt += 1

    x_ok = False
    y_ok = False

    if len(x_num) == 0:
        if X == 0:
            x_ok = True
    else:
        dp_x = [False] * N
        dp_x[0] = True
        for tx in x_num:
            for i in range(N - 1, -1, -1):
                if i + tx < N and dp_x[i]:
                    dp_x[i + tx] = True

        xsum = sum(x_num)
        for i in range(N):
            if dp_x[i]:
                if abs(i - abs(xsum - i)) == abs(X):
                    x_ok = True

    if len(y_num) == 0:
        if Y == 0:
            y_ok = True
    else:
        dp_y = [False] * N
        dp_y[0] = True
        for ty in y_num:
            for i in range(N - 1, -1, -1):
                if i + ty < N and dp_y[i]:
                    dp_y[i + ty] = True

        ysum = sum(y_num)
        for i in range(N):
            if dp_y[i]:
                if abs(i - abs(ysum - i)) == abs(Y):
                    y_ok = True

    # print(X, Y)
    # print(x_num)
    # print(y_num)

    if x_ok and y_ok:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
