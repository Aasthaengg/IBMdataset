# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, M, X, CA):
    ans = 10**10
    for p in range(1 << N):
        AA = [0] * (M + 1)
        C = 0
        for i in range(N):
            if p & (1 << i):
                C += CA[i][0]
                for j in range(1, M + 1):
                    AA[j] += CA[i][j]
        for i in range(1, M + 1):
            if AA[i] < X:
                break
        else:
            ans = min(ans, C)
    print(ans if ans < 10**10 else -1)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    CA = [tuple(map(int, input().split())) for _ in range(N)]
    main(N, M, X, CA)
