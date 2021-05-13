
def solve():
    Height = 10**9
    for i in range(0,N-K+1):
        hmax = h[i+K-1]
        hmin = h[i]
        Height = min(Height, hmax-hmin)
#        print(h[i:i+K])
#        print(Height)

    print(Height)

if __name__=="__main__":
    N,K = list(map(int, input().split()))
    h = [int(input()) for _ in range(N)]
    h.sort()
    solve()
