import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    xy = set(list(map(int, readline().split())))
    A = set([1,3,5,7,8,10,12])
    B = set([4,6,9,11])
    C = set([2])
    if xy<=A or xy<=B or xy<=C:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
