import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    edge = []
    for i in range(1, n):
        edge.append([1, i + 1])

    total = ((n - 1) * (n - 2)) // 2
    if k > total:
        print(-1)
        exit()

    diff = total - k
    while diff:
        for i in range(1, n):
            for j in range(i + 1, n):
                edge.append([i + 1, j + 1])
                diff -= 1
                if diff == 0:
                    break
            else:
                continue
            break

    print(len(edge))
    for res in edge:
        print(*res)


if __name__ == '__main__':
    resolve()
