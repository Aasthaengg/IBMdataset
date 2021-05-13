import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    INF = 10**8
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    key = [0]
    box = [0]
    for _ in range(M):
        k,_ = LI()
        key.append(k)
        b = 0
        for c in LI():
            b += 2**(c-1)
        box.append(b)

    dp = [[INF] * (2**N) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(1,M+1):
        for j in range(2**N):
            dp[i][j] = min(dp[i-1][j],dp[i-1][j - (j&box[i])]+key[i])
    if dp[-1][-1] == INF:
        print(-1)
    else:
        print(dp[-1][-1])
if __name__ == '__main__':
    main()