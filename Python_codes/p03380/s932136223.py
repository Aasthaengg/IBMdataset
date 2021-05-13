import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 998244353


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    MAX_V = A[-1]
    target = MAX_V // 2 if MAX_V % 2 == 0 else (MAX_V + 1) // 2

    diff = f_inf
    res = A[0]
    for i in range(n - 1):
        if abs(target - A[i]) < diff:
            diff = abs(target - A[i])
            res = A[i]
    print(MAX_V, res)


if __name__ == '__main__':
    resolve()
