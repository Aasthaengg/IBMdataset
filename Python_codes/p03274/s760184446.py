import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))
    len_m = len([x for x in X if x < 0])
    len_p = len([x for x in X if x > 0])
    ans = 10**10
    idx = max(0, len_m-K)
    s = [0] + X[idx:idx+K-1]
    for i in range(max(0, len_m-K), min(len_m+K, N-K+1)):
        s.pop(0)
        s.append(X[i+K-1])
        if s[0] < 0 and s[-1] > 0:
            c = min(abs(s[0]) * 2 + s[-1], abs(s[0]) + s[-1] * 2)
        else:
            c = max(abs(s[0]), abs(s[-1]))
        ans = min(ans, c)

    print(ans)


if __name__ == '__main__':
    main()