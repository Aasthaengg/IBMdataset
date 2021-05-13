import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    query = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1], reverse=True)

    B = []
    for i in range(m):
        b, c = query[i]
        while b and len(B) != n:
            B.append(c)
            b -= 1
    B.sort(reverse=True)

    for i in range(len(B)):
        if A[i] < B[i]:
            A[i] = B[i]
    print(sum(A))


if __name__ == '__main__':
    resolve()
