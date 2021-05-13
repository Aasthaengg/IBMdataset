import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    S = input()
    T = input()
    ans = N*2
    for i in range(N):
        s = S[i:]
        t = T[:N-i]
        if s == t:
            ans -= N-i
            break
    print(ans)

if __name__ == '__main__':
    main()