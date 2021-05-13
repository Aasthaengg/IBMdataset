def main():
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    mod=10**9+7
    ans=0
    for i in range(k-1,n):
        if i==k-1:
            c=1
        else:
            c=(c*i*pow(i-k+1,mod-2,mod))%mod
        ans+=(a[i]-a[n-i-1])*c
        ans%=mod
    print(ans)

if __name__ == '__main__':
    main()