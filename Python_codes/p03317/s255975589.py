import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = 1
    N -= K
    ans += (N + K - 2)//(K - 1)
    print(ans)
if __name__ == '__main__':
    main()