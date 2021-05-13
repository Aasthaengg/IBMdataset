import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    
    ans = 0
    for n in range(1, N+1):
        if len(str(n)) % 2:
            ans += 1
    
    print(ans)
    return


if __name__ == '__main__':
    main()
