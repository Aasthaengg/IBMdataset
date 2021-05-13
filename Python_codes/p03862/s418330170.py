from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,x=map(int,readline().split())
    a=list(map(int,readline().split()))

    ans=0
    for i in range(n):
        if i==0:
            if a[i]>x:
                ans+=a[i]-x
                a[i]=x
        else:
            if a[i-1]+a[i]>x:
                ans+=a[i]+a[i-1]-x
                a[i]-=a[i]+a[i-1]-x

    print(ans)
    
if __name__=="__main__":
    main()