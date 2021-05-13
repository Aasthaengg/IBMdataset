import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
