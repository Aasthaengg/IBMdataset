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


# 約数列挙 0(√N)
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = in_n()

    yaku = make_divisors(N)
    yaku.remove(1)

    ans = 0
    for x in yaku:
        tn = N
        while tn % x == 0:
            tn /= x
        if tn % x == 1:
            ans += 1

    yaku = make_divisors(N - 1)
    yaku.remove(1)
    ans += len(yaku)

    print(ans)


if __name__ == '__main__':
    main()
