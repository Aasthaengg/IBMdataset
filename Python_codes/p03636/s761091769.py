import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    L = len(S)
    ans = S[0] + str(L-2) + S[-1]
    print(ans)

if __name__ == '__main__':
    main()
