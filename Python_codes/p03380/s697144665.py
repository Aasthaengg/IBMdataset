import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    A.sort(reverse=True)
    n = max(A)
    med = n/2
    r = INF
    d = INF
    for a in A[1:]:
        if abs(a-med)<d:
            r = a
            d = abs(a-med)
    print(n,r)



if __name__ == '__main__':
    main()
