import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    S = input()
    sl = ['Sunny', 'Cloudy', 'Rainy']

    if S == 'Sunny':
        i = 1
    elif S == 'Cloudy':
        i = 2
    elif S == 'Rainy':
        i = 0

    print(sl[i])


if __name__ == '__main__':
    solve()
