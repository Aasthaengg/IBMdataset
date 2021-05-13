import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    print(max(A+B,A-B,A*B))




if __name__ == '__main__':
    main()
