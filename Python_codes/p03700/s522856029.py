import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, input().rstrip('\n').split()))
    h = [int(input().rstrip('\n')) for _ in range(n)]
    cor_v = 10 ** 16
    inc_v = -1
    while cor_v - inc_v > 1:
        bin_v = (cor_v + inc_v) // 2
        cost = 0
        #条件を満たすcostを全検索
        for i in range(n):
            hp = h[i] - bin_v * b
            if hp > 0:
                cost += (hp + (a - b) - 1) // (a - b)
        #costが制約を満たすか
        if cost <= bin_v:
            cor_v = bin_v
        else:
            inc_v = bin_v
    print(cor_v)


if __name__ == '__main__':
    solve()
