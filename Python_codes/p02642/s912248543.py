from collections import Counter


def solve(string):
    n, *a = map(int, string.split())
    table = [True] * (10**6 + 1)
    ma = max(a)
    for _a in a:
        if table[_a]:
            for i in range(2 * _a, ma + 1, _a):
                table[i] = False
    return str(sum(table[k] for k, v in Counter(a).items() if v == 1))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
