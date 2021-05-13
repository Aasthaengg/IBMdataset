import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    h, w, a, b = list(map(int, input().rstrip('\n').split()))
    for i in range(h):
        if i < b:
            print("".join(["0"] * a + ["1"] * (w - a)))
        else:
            print("".join(["1"] * a + ["0"] * (w - a)))


if __name__ == '__main__':
    solve()
