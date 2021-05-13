N = int(input())
K = int(input())
X = list(map(int, input().split()))


def diff_ball_K(N, K):
    return [N - K]


ball_K = list(map(lambda x: K - x, X))



diff = [min(a,b) for a,b in zip(X, ball_K)]
print(sum(diff)*2)