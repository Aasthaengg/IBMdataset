import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**19
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,K = LI()
    px = [LI() for _ in range(N)]
    px.sort()

    ans = INF
    for k in range(K,N+1):
        for i in range(N-k+1):
            w = px[i+k-1][0] - px[i][0]
            py = []
            for _,y in px[i:i+k]:
                py.append(y)
            py.sort()
            min_y = INF
            for j in range(k-K+1):
                min_y = min(min_y,py[K+j-1]-py[j])
            ans = min(ans,w * min_y)
    print(ans)

if __name__ == '__main__':
    main()