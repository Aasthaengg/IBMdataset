import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    B = [[] for _ in range(N)]
    for i in range(N):
        k = int(readline())
        for _ in range(k):
            x, y = map(int, readline().split())
            B[i].append((x - 1, y))

    ans = 0
    for bit in range(1 << N):
        ok = True
        for i in range(N):
            if not (bit & (1 << i)):
                continue
            for x, y in B[i]:
                if bool(bit & (1 << x)) != bool(y):
                    ok = False
                    break
            if not ok:
                break

        if ok:
            ans = max(ans, str(bin(bit)).count('1'))

    print(ans)
    return


if __name__ == '__main__':
    main()
