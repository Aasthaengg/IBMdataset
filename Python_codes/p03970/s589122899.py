import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    A = 'CODEFESTIVAL2016'
    ans = 0
    for s, a in zip(S,A):
        if s!=a:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
