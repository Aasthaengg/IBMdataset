import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())

    n = 0

    def dfs(vec, d):
        nonlocal n
        if d == 0:
            n += 1
            if n == K:
                print(''.join(map(str, vec)))
                return
            else:
                return

        for i in range(max(0, vec[-1] - 1), min(9, vec[-1] + 1) + 1):
            vec.append(i)
            dfs(vec, d - 1)
            if n >= K:
                return
            vec.pop()

    for d in range(10 ** 20):
        for i in range(1, 10):
            vec = [i]
            dfs(vec, d)
            if n >= K:
                return

    return


if __name__ == '__main__':
    main()
