import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s = str(readline().rstrip().decode('utf-8'))
    w = int(readline())
    ans = []
    for i in range(0, len(s), w):
        ans.append(s[i])
    print("".join(ans))


if __name__ == '__main__':
    solve()
