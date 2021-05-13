import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S1 = readline().strip()
    S2 = readline().strip()
    
    if S1 == S2[::-1]:
        print('YES')
    else:
        print('NO')
    
    return


if __name__ == '__main__':
    main()
