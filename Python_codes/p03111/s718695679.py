import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, A, B, C = in_nn()
    l = list(map(int, read().rstrip().split()))

    comb = list(itertools.product(range(4), repeat=N))
    ans = 10**9 + 7

    for c in comb:
        if (0 in c) and (1 in c) and (2 in c):
            t = [0] * 3
            m = [-10] * 3
            for i in range(N):
                if c[i] == 3:
                    continue
                t[c[i]] += l[i]
                m[c[i]] += 10

            m[0] += abs(t[0] - A)
            m[1] += abs(t[1] - B)
            m[2] += abs(t[2] - C)

            ans = min(ans, sum(m))

    print(ans)


if __name__ == '__main__':
    main()
