import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    K,A,B = map(int,input().split())
    if B - A >= 2:
        K -= A - 1
        ans = A + (B - A) * (K//2) + K%2
    else:
        ans = K + 1
    print(ans)
if __name__ == '__main__':
    main()