import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())

    """
    奇数人のときは１飛ばし、３飛ばし、５飛ばし、、、とすればよい。
    偶数人のときは１飛ばし、３飛ばし、、、で途中から偶数飛ばしに切り替えるとよい。
    （「カークマンの組み分け」を参照）
    構成問題苦手だ。。。
    """

    if N % 2 == 1:
        cnt = 0
        for l in range(1, N // 2 + 1):
            r = N - l + 1
            print("{} {}".format(l, r))
            cnt += 1
            if cnt == M: return
    else:
        cnt = 0
        for l in range(1, N // 4 + 1):
            r = N - l + 1
            print("{} {}".format(l, r))
            cnt += 1
            if cnt == M: return
        for l in range(N // 4 + 1, N // 2):
            r = N - l
            print("{} {}".format(l, r))
            cnt += 1
            if cnt == M: return

    

if __name__ == "__main__":
    main()