import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A, B = map(int, readline().split())
    P = list(map(int, readline().split()))
    a = 0
    b = 0
    c = 0
    for p in P:
        if p<=A:
            a += 1
        elif A<p<=B:
            b += 1
        else:
            c += 1
    print(min(a,b,c))

if __name__ == '__main__':
    main()
