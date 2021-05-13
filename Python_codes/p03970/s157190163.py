import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s = str(readline().rstrip().decode('utf-8'))
    cs = "CODEFESTIVAL2016"
    cnt = 0
    for i in range(len(cs)):
        if s[i] != cs[i]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
