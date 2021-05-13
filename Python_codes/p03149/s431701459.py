import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = list(map(int, readline().split()))
    N.sort()
    if N==[1,4,7,9]:
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':
    main()
