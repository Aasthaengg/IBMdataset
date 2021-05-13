from sys import stdin
def main():
    #入力
    readline=stdin.readline
    mod=10**9+7
    n,m=map(int,readline().split())
    
    if n==m:
        ans=2*(f(n,mod))**2
    elif n==m-1 or m==n-1:
        ans=f(n,mod)*f(m,mod)
    else:
        ans=0
    ans%=mod
    print(ans)
    
def f(n,mod):
    res=1
    for i in range(1,n+1):
        res*=i
        res%=mod
    return res
    
if __name__=="__main__":
    main()