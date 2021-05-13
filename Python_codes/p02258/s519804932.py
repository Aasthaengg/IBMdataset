from sys import stdin
 
inf = 10**9 + 1

def solve():
    n = int(stdin.readline())
    max_d = -inf
    min_v = inf * 2

    for i in range(n):
        r = int(stdin.readline())

        max_d = max(max_d, r - min_v)
        min_v = min(min_v, r)

    print(max_d)


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None
 
if __name__ == '__main__':
    solve()