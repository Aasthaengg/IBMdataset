import sys
import copy

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

    N = in_n()
    A = in_nl()

    def solve():

        ta = copy.copy(A)
        cnt1 = 0

        if ta[0] <= 0:
            t = -ta[0] + 1
            cnt1 += t
            ta[0] += t

        sum_a = ta[0]
        for i in range(1, N):
            if i % 2 == 0:
                if sum_a + ta[i] <= 0:
                    t = -(sum_a + ta[i]) + 1
                    cnt1 += t
                    ta[i] += t
            else:
                if sum_a + ta[i] >= 0:
                    t = sum_a + ta[i] + 1
                    cnt1 += t
                    ta[i] -= t
            sum_a += ta[i]

        #####

        ta = copy.copy(A)
        cnt2 = 0

        if ta[0] >= 0:
            t = ta[0] + 1
            cnt2 += t
            ta[0] -= t

        sum_a = ta[0]
        for i in range(1, N):
            if i % 2 == 1:
                if sum_a + ta[i] <= 0:
                    t = -(sum_a + ta[i]) + 1
                    cnt2 += t
                    ta[i] += t
            else:
                if sum_a + ta[i] >= 0:
                    t = sum_a + ta[i] + 1
                    cnt2 += t
                    ta[i] -= t
            sum_a += ta[i]

        return min(cnt1, cnt2)

    ans = solve()
    print(ans)


if __name__ == '__main__':
    main()
