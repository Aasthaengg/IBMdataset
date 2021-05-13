# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    idx = [0] * N
    D = [[-1] * (N) for _ in range(N)]
    for j in range(N):
        D[j][0] = 0
    while True:
        f = True
        for i in range(N):
            if idx[i] >= N - 1: continue
            m = A[i][idx[i]]
            if A[m][idx[m]] == i:
                d = max(D[i][idx[i]], D[m][idx[m]])
                idx[i] += 1
                idx[m] += 1
                D[i][idx[i]] = d + 1
                D[m][idx[m]] = d + 1
                f = False
        if f: break
    ans = -1
    for i in range(N):
        ans = max(ans, D[i][N - 1])
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(N)]
    main(N, A)
