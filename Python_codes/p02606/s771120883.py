import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    L, R, d = map(int, rl().split())
    
    ans = 0
    for i in range(L, R + 1):
        if i % d == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()