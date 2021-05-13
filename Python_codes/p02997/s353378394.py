# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap



@mt
def slv(N, K):
    from itertools import combinations
    ans = [(1, i) for i in range(2, N+1)]

    K -= (N-1)*(N-2) // 2
    if K > 0:
        print(-1)
        return
    for i, j in combinations(range(2, N+1), r=2):
        if K == 0:
            break
        ans.append((i, j))
        K += 1


    print(len(ans))
    for uv in ans:
        print(*uv)



def main():
    N, K = read_int_n()
    slv(N, K)


if __name__ == '__main__':
    main()
