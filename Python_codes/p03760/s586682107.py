import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    O = readline().strip()
    E = readline().strip()

    ans = ''.join(O[i // 2] if i % 2 == 0 else E[i // 2] for i in range(len(O) + len(E)))
    print(ans)
    return


if __name__ == '__main__':
    main()
