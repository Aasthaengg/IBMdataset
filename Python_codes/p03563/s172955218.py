# run on python 3.4.3

from sys import stdin


def main():
    r = int(stdin.readline())
    g = int(stdin.readline())
    ans = g * 2 - r
    print(ans)


main()
