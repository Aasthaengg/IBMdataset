# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, C, XV):
    rXV = [(C - x, v) for x, v in reversed(XV)]
    ans1 = solve(N, C, XV, rXV)
    ans2 = solve(N, C, rXV, XV)
    print(max(ans1, ans2))

def solve(N, C, XV, rXV):
    M = [0]
    px = 0
    now = 0
    tmp = 0
    for x, v in rXV:
        now += v - (x - px)
        tmp = max(tmp, now)
        M.append(tmp)
        px = x

    res = 0
    px = 0
    now = 0
    for i, (x, v) in enumerate(XV):
        now += v - (x - px)
        res = max(res, now)
        res = max(res, now - x + M[N - i - 1])
        px = x
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    N, C = map(int, input().split())
    XV = [tuple(map(int, input().split())) for _ in range(N)]
    main(N, C, XV)
