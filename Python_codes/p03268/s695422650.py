import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    cnt0 = cntk = 0
    for num in range(1, n + 1):
        if num % k == 0:
            cnt0 += 1
        elif num % k == k // 2:
            cntk += 1

    if k % 2 == 0:
        res = pow(cnt0, 3) + pow(cntk, 3)
    else:
        res = pow(cnt0, 3)
    print(res)


if __name__ == '__main__':
    resolve()
