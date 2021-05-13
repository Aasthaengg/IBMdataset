def solve(a,k):
    dp=[0]*(k+1)
    for i in range(k+1):
        for j in a:
            if i>=j and not dp[i-j]:
                dp[i]=1
    return 'First' if dp[-1] else 'Second'
if __name__=='__main__':
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(solve(a,k))