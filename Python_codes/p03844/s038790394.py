import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, op, B = input().split()
    if op=='+':
        print(int(A)+int(B))
    else:
        print(int(A)-int(B))


if __name__ == '__main__':
    main()
