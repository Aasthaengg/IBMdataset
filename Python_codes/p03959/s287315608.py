import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))

    check = [False] * n
    check[0] = check[-1] = True
    res = [f_inf] * n
    res[0] = T[0]
    res[-1] = A[-1]
    for i in range(1, n):
        if T[i - 1] != T[i] or T[i] == 1:
            check[i] = True
        res[i] = min(res[i], T[i])

    for j in reversed(range(n - 1)):
        if A[j + 1] != A[j] or A[j] == 1:
            check[j] = True
        res[j] = min(res[j], A[j])

    ma = 0
    for i in range(n):
        if check[i]:
            if res[i] > ma:
                ma = res[i]
        if T[i] > ma:
            print(0)
            exit()

    ma = 0
    for i in reversed(range(n)):
        if check[i]:
            if res[i] > ma:
                ma = res[i]
        if A[i] > ma:
            print(0)
            exit()

    ans = 1
    for k in range(n):
        if not check[k]:
            ans *= res[k]
            ans %= mod
    print(ans)


if __name__ == '__main__':
    resolve()
