import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readlines()
    trans = str.maketrans('abc', '012')
    S = [list(map(int, s.strip().translate(trans)))[::-1] for s in S]

    i = 0
    while S[i]:
        i = S[i].pop()

    player = 'ABC'

    print(player[i])
    return


if __name__ == '__main__':
    main()
