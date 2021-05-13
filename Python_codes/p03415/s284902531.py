import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    C = read().split()
    ans = ''
    for i in range(3):
        ans += C[i][i]
    print(ans)


if __name__ == '__main__':
    main()
