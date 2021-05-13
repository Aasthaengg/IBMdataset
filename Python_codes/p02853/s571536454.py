import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    x, y = list(map(int, readline().split()))
    if x == 1 and y == 1:
        print(300000 * 2 + 400000)
    else:
        t = 0
        if x == 1:
            t += 300000
        elif x == 2:
            t += 200000
        elif x == 3:
            t += 100000
            
        if y == 1:
            t += 300000
        elif y == 2:
            t += 200000
        elif y == 3:
            t += 100000
        print(t)


if __name__ == '__main__':
    solve()
