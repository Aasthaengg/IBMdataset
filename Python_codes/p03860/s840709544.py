import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, x, B = input().split()
    ans = A[0] + x[0] + B[0]
    print(ans.upper())



if __name__ == '__main__':
    main()
