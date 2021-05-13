import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    idx = S.find('C')
    if idx == -1:
        print('No')
    else:
        i = S[idx:].find('F')
        if i == -1:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    main()
