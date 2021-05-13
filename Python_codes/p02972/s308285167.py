# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    A = [-1] + A
    B = [0] * (N + 1)
    for i in range(N, 0, -1):
        xor = 0
        for j in range(i * 2, N + 1, i):
            xor ^= B[j]
        B[i] = xor ^ A[i]
    print(sum(B))
    print(*[i for i, b in enumerate(B) if b == 1])

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
