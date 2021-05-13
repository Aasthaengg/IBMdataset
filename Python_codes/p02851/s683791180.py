from collections import defaultdict


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * (N+1)
    for i, a in enumerate(A):
        X[i+1] = (X[i] + a - 1) % K
    cnt = defaultdict(int)
    ans = 0
    for i in range(N+1):
        if i >= K:
            cnt[X[i-K]] -= 1
        ans += cnt[X[i]]
        cnt[X[i]] += 1
    print(ans)


if __name__ == "__main__":
    main()
