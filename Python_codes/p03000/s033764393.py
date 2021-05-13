import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, X, *L = map(int, read().split())
    
    ans = 1
    d = 0
    for l in L:
        d += l
        if d <= X:
            ans += 1
        else:
            break
    
    print(ans)
    return


if __name__ == '__main__':
    main()
