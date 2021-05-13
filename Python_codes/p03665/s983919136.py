import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))
    odd = len([a for a in A if a % 2 != 0])
    even = len([a for a in A if a % 2 == 0])

    # 奇数のビスケットが入った袋を偶数個(０を除く）選ぶパターン
    tot_odd = 0
    for i in range(2, odd + 1, 2):
        bunbo = 1
        bunsi = 1
        for j in range(1, i + 1):
            bunbo *= (odd - j + 1)
            bunsi *= j
        cmb = bunbo // bunsi
        tot_odd += cmb

    # 偶数のビスケットが入った袋を選ぶパターン
    tot_even = 0
    for i in range(even + 1):
        if i == 0:
            tot_even += 1
            continue
        bunbo = 1
        bunsi = 1
        for j in range(1, i + 1):
            bunbo *= (even - j + 1)
            bunsi *= j
        cmb = bunbo // bunsi
        tot_even += cmb

    even_pattern = tot_odd * tot_even + tot_even
    odd_pattern = 2 ** n - even_pattern
    print(even_pattern if p == 0 else odd_pattern)


if __name__ == '__main__':
    resolve()
