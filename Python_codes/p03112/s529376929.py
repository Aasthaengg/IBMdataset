import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')

INF = 10**12
d = lambda a, b: abs(a - b)


def main():

    A, B, Q = in_nn()
    tmp = list(map(int, read().split()))
    s = tmp[:A]
    t = tmp[A:A + B]
    x = tmp[A + B:]

    a = [0] * Q

    for i in range(Q):

        n = x[i]

        if n <= s[0]:
            a1 = -INF
            a2 = s[0]
        elif n >= s[-1]:
            a1 = s[-1]
            a2 = INF
        else:
            si = bisect.bisect_right(s, n)
            a1 = s[si - 1]
            a2 = s[si]

        if n <= t[0]:
            b1 = -INF
            b2 = t[0]
        elif n >= t[-1]:
            b1 = t[-1]
            b2 = INF
        else:
            ti = bisect.bisect_right(t, n)
            b1 = t[ti - 1]
            b2 = t[ti]

        # print(a1, a2, b1, b2)
        ans = d(n, a1) + min(d(a1, b1), d(a1, b2))
        ans = min(ans, d(n, a2) + min(d(a2, b1), d(a2, b2)))
        ans = min(ans, d(n, b1) + min(d(b1, a1), d(b1, a2)))
        ans = min(ans, d(n, b2) + min(d(b2, a1), d(b2, a2)))
        a[i] = ans

    print('\n'.join(map(str, a)))


if __name__ == '__main__':
    main()
