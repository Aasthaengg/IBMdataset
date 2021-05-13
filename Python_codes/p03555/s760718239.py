import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    C = read().split()
    for i in range(3):
        if C[0][i] != C[1][2-i]:
            print('NO')
            break
    else:
        print('YES')


if __name__ == '__main__':
    main()
