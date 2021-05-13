import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    D,N = map(int,input().split())
    if N != 100:
        ans = N * pow(100,D)
    else:
        ans = 101 * pow(100,D)
    print(ans)
if __name__ == '__main__':
    main()
