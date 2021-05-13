import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    K, A, B = map(int, input().split())
    cnt = 0
    if B - A >= 3:
        times = (K - (A - 1)) // 2
        if times >= 1:
            cnt += A
            cnt+=(B-A)*times
            if (K - (A - 1)) // 2 == (K - (A - 1)) / 2:
                pass
            else:
                cnt += 1
        else:
            cnt = 1 + K
    else:
        cnt = 1 + K

    print(cnt)


resolve()