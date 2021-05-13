import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    BC = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: -x[1])
    C = []
    for b, c in BC:
        if len(C) >= n:
            break
        C += [c] * b
    A += C
    A.sort(reverse=True)
    res = sum(A[:n])
    print(res)


if __name__ == '__main__':
    resolve()
