import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def check(vec, init_pos, target_pos):
    base = 8000
    dp = [False] * 16001
    dp[init_pos + base] = True

    for i in range(len(vec)):
        dp, dp_prev = [False] * 16001, dp
        for j in range(16001):
            if (
                j - vec[i] >= 0
                and dp_prev[j - vec[i]]
                or j + vec[i] <= 16000
                and dp_prev[j + vec[i]]
            ):
                dp[j] = True

    return dp[target_pos + base]


def main():
    S = readline().strip()
    x, y = map(int, readline().split())

    idx = len(S)
    for i, c in enumerate(S):
        if c == 'T':
            idx = i
            break

    init_x = idx
    step = [[] for _ in range(2)]
    i = 0
    for c in S[idx:]:
        if c == 'T':
            i = 1 - i
            step[i].append(0)
        else:
            step[i][-1] += 1
            
    for row in step:
        row = [v for v in row if v != 0]
        if not row:
            row = [0]

    ok = check(step[0], init_x, x) and check(step[1], 0, y)

    if ok:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
