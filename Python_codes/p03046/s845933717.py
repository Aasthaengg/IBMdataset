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
def slv(M, K):
    if K >= 2**(M+1):
        return [-1]

    if K == 0:
        ans = []
        for i in range(2**M):
            ans.append(i)
            ans.append(i)
        return ans

    p = []
    done = set()
    for a in range(2**M):
        if a in done:
            continue
        b = K ^ a
        if b >= 2**M:
            return [-1]
        p.append((a, b))
        done.add(a)
        done.add(b)

    if len(p) % 2 != 0:
        return [-1]

    ans = []
    for i in range(0, len(p), 2):
        a, b = p[i]
        c, d = p[i+1]
        ans.append(a)
        ans.append(b)
        ans.append(c)
        ans.append(d)
        ans.append(b)
        ans.append(a)
        ans.append(d)
        ans.append(c)

    return ans



def main():
    M, K = read_int_n()
    print(*slv(M, K))


if __name__ == '__main__':
    main()
