import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, K = map(int, readline().split())
    for i in range(K):
        if i%2==0:
            if A%2==1:
                A -= 1
            B += A//2
            A //= 2
        else:
            if B%2==1:
                B -= 1
            A += B//2
            B //= 2
    print(A, B)


if __name__ == '__main__':
    main()
