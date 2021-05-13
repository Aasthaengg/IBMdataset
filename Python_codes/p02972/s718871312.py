import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = [0] + list(map(int, readline().split()))
    B = [0] * (N + 1)
    ans = []
    for i in range(N, 0, -1):
        x = sum(B[i::i])
        if x % 2 == A[i]:
            continue
        else:
            B[i] = 1
            ans.append(str(i))
    print(len(ans))
    print(' '.join(ans))


if __name__ == '__main__':
    main()
