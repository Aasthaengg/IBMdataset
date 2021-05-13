import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for a in A:
        while a%2 == 0:
            ans += 1
            a >>= 1
    print(ans)
if __name__ == '__main__':
    main()