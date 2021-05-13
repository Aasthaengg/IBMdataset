import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    T = readline().strip()
    
    ans = 0
    for s, t in zip(S, T):
        if s == t:
            ans += 1
            
    print(ans)
    return


if __name__ == '__main__':
    main()
