import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    main()
