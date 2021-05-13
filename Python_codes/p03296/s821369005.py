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
    for i in range(1,N):
        if A[i] == A[i-1]:
            count += 1
            A[i] = -1
    print(count)

if __name__ == '__main__':
    main()
