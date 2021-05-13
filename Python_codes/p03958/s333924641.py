import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(t):
        B.append([i + 1, A[i]])
    B = sorted(B, key=lambda x: x[1])

    if t == 1:
        print(k - 1)
        exit()

    res = 0
    pre = 0
    for i in range(k):
        if pre != B[-1][0]:
            pre = B[-1][0]
            B[-1][1] -= 1
            B = sorted(B, key=lambda x: x[1])
        else:
            if B[-2][1] != 0:
                pre = B[-2][0]
                B[-2][1] -= 1
                B = sorted(B, key=lambda x: x[1])
            else:
                B[-1][1] -= 1
                res += 1

    print(res)


if __name__ == '__main__':
    resolve()
