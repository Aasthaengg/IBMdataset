import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()

    ans = 0

    for i in range(N):
        x, u = readline().rstrip().split()
        x = float(x)
        u = u.decode()
        if u == 'JPY':
            ans += x
        elif u == 'BTC':
            ans += x * 380000

    print(ans)


if __name__ == '__main__':
    main()
