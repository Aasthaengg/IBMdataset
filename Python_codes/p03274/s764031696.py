import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    idx = bisect_left(X, 0)
    #print("idx={}".format(idx))
    ans = 10**10
    if idx == N:
        print(-X[-K])
        return
    elif 0 == X[idx]:
        for i in range(idx + 1):
            num = idx - i + 1
            if num > K: continue
            elif num == K: ans = min(ans, -X[i])
            elif 0 <= idx + (K - num) and idx + (K - num) < N:
                ans = min(ans, -2 * X[i] + X[idx + (K - num)])
        for i in range(idx + 1, N):
            num = i - idx + 1
            if num > K: continue
            elif num == K: ans = min(ans, X[i])
            elif 0 <= idx - (K - num) and idx - (K - num) < N:
                ans = min(ans, 2 * X[i] - X[idx - (K - num)])
    else:
        for i in range(idx):
            num = idx - i
            if num > K: continue
            elif num == K: ans = min(ans, -X[i])
            elif 0 <= idx + (K - num) - 1 and idx + (K - num) - 1 < N:
                ans = min(ans, -2 * X[i] + X[idx + (K - num) - 1])
            #print("i={}, num={}, cand={}, ans={}".format(i, idx - (K - num) - 1, -2 * X[i] + X[idx + (K - num) - 1], ans))
        for i in range(idx, N):
            num = i - idx + 1
            if num > K: continue
            elif num == K: ans = min(ans, X[i])
            elif 0 <= idx - (K - num) and idx - (K - num) < N:
                ans = min(ans, 2 * X[i] - X[idx - (K - num)])
            #print("i={}, ans={}".format(i, ans))
    print(ans)

if __name__ == "__main__":
    main()
