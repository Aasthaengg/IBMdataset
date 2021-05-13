def f():
    import sys
    input=sys.stdin.buffer.readline
    sys.setrecursionlimit(10**9)
    h,w,k=map(int,input().split())
    dp=[0]*w
    dp[k-1]=1
    ne=[0]*w
    mod=10**9+7
    table=[1,1,2,3,5,8,13,21,34]
    for c in range(h):
        for i in range(w):
            ne[i]=dp[i]*table[i]*table[w-i-1]
            if i>0:
                ne[i]+=dp[i-1]*table[i-1]*table[w-i-1]
            if i<w-1:
                ne[i]+=dp[i+1]*table[i]*table[w-i-2]
            ne[i]%=mod
        dp,ne=ne,dp
    print(dp[0])


if __name__ == "__main__":
    f()