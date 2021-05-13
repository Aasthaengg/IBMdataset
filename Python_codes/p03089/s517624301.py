import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
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
                b = B.pop(j)
                res.append(b)
                break
        else:
            print(-1)
            break
    else:
        print(*res[::-1], sep="\n")


if __name__ == '__main__':
    resolve()
