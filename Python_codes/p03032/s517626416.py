import sys
input = sys.stdin.readline

def read():
    N, K = map(int, input().strip().split())
    V = list(map(int, input().strip().split()))
    return N, K, V


def solve(N, K, V):
    ans = 0
    for k in range(min(K, N) + 1):
        for l in range(0, k+1):
            s = sorted(V[:l] + V[N-k+l:])
            v = sum(s)
            ans = max(ans, v)
            if k < K:
                # 最大(min(K-k, k))回、キューに戻すことが可能
                # 負の数は戻せるだけ戻せばよい
                for m in range(min(K-k, k)):
                    if s[m] < 0:
                        v -= s[m]
                ans = max(ans, v)

    return ans


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
