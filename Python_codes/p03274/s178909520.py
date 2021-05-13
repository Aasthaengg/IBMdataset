
def solve():
    ans = float("inf")
#    print(x[2])
    for i in range(N-K+1):
        #print(i)
        ans = min(ans, abs(x[i])+abs(x[i]-x[i+K-1]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    print(ans)

if __name__=="__main__":
    N,K = list(map(int, input().split()))
    x = list(map(int, input().split()))
    solve()

