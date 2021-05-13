import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A = int(readline())
    B = int(readline())
    C = int(readline())
    D = int(readline())
    
    print(min(A,B)+min(C,D))


if __name__ == '__main__':
    main()
