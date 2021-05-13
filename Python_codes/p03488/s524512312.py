import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def check(vec, init_pos, target_pos):
    dp = {init_pos}

    for nv in vec:
        if nv == 0:
            continue
        dp_next = set()
        for v in dp:
            dp_next.add(v - nv)
            dp_next.add(v + nv)
        dp = dp_next

    return target_pos in dp


def main():
    S = readline().strip()
    x, y = map(int, readline().split())

    L = [len(commands) for commands in S.split('T')]

    init_x = L[0]
    x_commands = L[2::2]
    y_commands = L[1::2]

    ok = check(x_commands, init_x, x) and check(y_commands, 0, y)

    if ok:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
