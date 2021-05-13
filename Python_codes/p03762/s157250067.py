def main():
    n,m=map(int,input().split())
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    mod=10**9+7
    s=[(s[i+1]-s[i])*(i+1)*(n-i-1)%mod for i in range(n-1)]
    t=[(t[i+1]-t[i])*(i+1)*(m-i-1)%mod for i in range(m-1)]
    print(sum(s)*sum(t)%mod)
main()