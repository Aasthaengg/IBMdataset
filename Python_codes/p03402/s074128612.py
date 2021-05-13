import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    res = [["."] * 100 for _ in range(100)]
    for h in range(50, 100):
        for w in range(100):
            res[h][w] = "#"

    for h in range(0, 100, 2):
        for w in range(0, 100, 2):
            if b == 1:
                break
            res[h][w] = "#"
            b -= 1
        else:
            continue
        break

    for h in reversed(range(0, 100, 2)):
        for w in range(0, 100, 2):
            if a == 1:
                break
            res[h][w] = "."
            a -= 1
        else:
            continue
        break

    print(100, 100)
    for i in res:
        print("".join(i))


if __name__ == '__main__':
    resolve()
