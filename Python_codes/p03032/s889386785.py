def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    V.insert(0, 0)
    ans = 0
    for i in range(min(N+1, K+1)):
        for j in range(min(N+1, K+1)):
            if i + j > min(N, K):
                break
            if i == j == 0:
                continue
            minus_l = []
            sum_v = 0
            for ii in range(i+1):
                v = V[ii]
                if v < 0:
                    minus_l.append(v)
                sum_v += v
            for jj in range(j+1):
                v = V[-jj]
                if v < 0:
                    minus_l.append(v)
                sum_v += v
            minus_l.sort(reverse=True)
            for x in range(K-i-j):
                if minus_l:
                    sum_v -= minus_l.pop()
                else:
                    break
            ans = max(ans, sum_v)
    print(ans)
if __name__ == '__main__':
    main()