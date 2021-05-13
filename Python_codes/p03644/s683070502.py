import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    
    
    for n in range(N, 0, -1):
        m = n
        while m % 2 == 0:
            m //= 2
        if m == 1:
            ans = n
            break
        
    print(ans)
    return


if __name__ == '__main__':
    main()
