import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))
    A.sort()
    if A[0] == A[1]:
        print(A[2])
    else:
        print(A[0])
    
    return


if __name__ == '__main__':
    main()
