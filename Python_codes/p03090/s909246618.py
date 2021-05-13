import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    cnt = n
    if n % 2:
        cnt -= 1

    edge = []
    for i in range(n):
        for j in range(i + 1, n):
            if j + 1 == cnt:
                continue
            edge.append([i + 1, j + 1])
        cnt -= 1

    print(len(edge))
    for res in edge:
        print(*res)


if __name__ == '__main__':
    resolve()
