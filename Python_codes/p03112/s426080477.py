import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')

INF = 10**12


def main():

    A, B, Q = in_nn()
    tmp = list(map(int, read().split()))
    s = [-INF] + tmp[:A] + [INF]
    t = [-INF] + tmp[A:A + B] + [INF]
    x = tmp[A + B:]

    a = [0] * Q
    d = lambda a, b: abs(a - b)

    for i in range(Q):

        n = x[i]

        si = bisect.bisect_right(s, n)
        a1 = s[si - 1]
        a2 = s[si]

        ti = bisect.bisect_right(t, n)
        b1 = t[ti - 1]
        b2 = t[ti]

        ans = d(n, a1) + min(d(a1, b1), d(a1, b2))
        ans = min(ans, d(n, a2) + min(d(a2, b1), d(a2, b2)))
        ans = min(ans, d(n, b1) + min(d(b1, a1), d(b1, a2)))
        ans = min(ans, d(n, b2) + min(d(b2, a1), d(b2, a2)))
        a[i] = ans

    print('\n'.join(map(str, a)))


if __name__ == '__main__':
    main()
