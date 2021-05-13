import sys
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = str(readline().rstrip().decode('utf-8'))
    b = str(readline().rstrip().decode('utf-8'))
    c = str(readline().rstrip().decode('utf-8'))
    cnt = 0
    for i in range(n):
        ct = collections.Counter([a[i], b[i], c[i]])
        if len(ct) == 3:
            cnt += 2
        elif len(ct) == 2:
            cnt += 1
        elif len(ct) == 1:
            cnt += 0
    print(cnt)


if __name__ == '__main__':
    solve()
