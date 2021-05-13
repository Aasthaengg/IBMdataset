import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))
    
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')
    
    return


if __name__ == '__main__':
    main()
