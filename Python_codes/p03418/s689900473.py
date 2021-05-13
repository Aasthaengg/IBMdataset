def solve():
    N, K = map(int,input().split())
    ans = 0
    for b in range(1,N+1):
        ans += max(0,(N//b) * (b-K)) 
        ans += max(0, N%b - K+1)
    
    if K == 0:
        ans -= N
    
    print(ans)

if __name__ == '__main__':
    solve()