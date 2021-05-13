import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt_2 = 0
    cnt_4 = 0
    for i in range(n):
        if A[i] % 4 == 0:
            cnt_4 += 1
        elif A[i] % 2 == 0:
            cnt_2 += 1

    if (n - max(0, cnt_2 - 1)) // 2 <= cnt_4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    resolve()
