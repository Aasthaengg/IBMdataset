import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    count = 0
    for a in A:
        if a%2==1:
            count += 1
    if count%2==1:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
