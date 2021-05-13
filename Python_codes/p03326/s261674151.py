import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, M = in_nn()
    t = in_na()
    cake = list(zip(t, t, t))

    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c = []
                for x, y, z in cake:
                    if i == 1:
                        x = -x
                    if j == 1:
                        y = -y
                    if k == 1:
                        z = -z
                    c.append(x + y + z)
                c.sort(reverse=True)
                ans = max(ans, sum(c[:M]))

    print(ans)


if __name__ == '__main__':
    main()
