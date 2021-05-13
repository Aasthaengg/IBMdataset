import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    B = list(map(int, input().split()))

    res = []
    while B:
        for i in reversed(range(len(B))):
            if B[i] == i + 1:
                b = B.pop(i)
                res.append(b)
                break
        else:
            print(-1)
            exit()
    print(*res[::-1], sep="\n")


if __name__ == '__main__':
    resolve()
