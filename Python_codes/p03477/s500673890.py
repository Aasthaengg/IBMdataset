import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C, D = map(int, readline().split())
    if A + B > C + D:
        print('Left')
    elif A + B == C + D:
        print('Balanced')
    else:
        print('Right')


if __name__ == '__main__':
    main()
