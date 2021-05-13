def ball_distribution(N: int, K: int)->int:
    if K == 1:
        return 0
    return N-K


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = ball_distribution(N, K)
    print(ans)
