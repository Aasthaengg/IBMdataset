def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 18
    for i in range(K-1, N):
        a = X[i-K+1]
        b = X[i]
        if a < 0 and b > 0:
            ans = min(ans, (-a)*2+b, (-a)+b*2)
        elif b <= 0:
            ans = min(ans, -a)
        elif a >= 0:
            ans = min(ans, b)
    print(ans)





if __name__ == '__main__':
    main()