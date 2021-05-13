import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = readline().decode('utf-8').strip()
    w = int(readline())
    ans = ''
    for i in range(0, len(S), w):
        ans += S[i]
    print(ans)


if __name__ == '__main__':
    main()
