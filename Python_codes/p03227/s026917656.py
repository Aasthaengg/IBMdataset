import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    if len(S)==2:
        print(S)
    else:
        print(''.join(list(reversed(S))))


if __name__ == '__main__':
    main()
