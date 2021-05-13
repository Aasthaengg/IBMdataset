import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C = map(str, readline().decode('utf-8').strip().split())
    if A[-1]==B[0] and B[-1]==C[0]:
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':
    main()
