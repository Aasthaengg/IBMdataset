import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    B = list(map(int, input().split()))

    res = []
    for i in range(n):
        L = len(B)
        for j in reversed(range(L)):
            if j + 1 == B[j]:
                res.append(B[j])
                B.pop(j)
                break
        else:
            print(-1)
            exit()

    res = res[::-1]
    for i in res:
        print(i)


if __name__ == '__main__':
    resolve()
