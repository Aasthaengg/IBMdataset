from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,a,b=map(int,readline().split())
    x=list(map(int,readline().split()))
    y=[0]*(n-1)
    for i in range(n-1):
        y[i]=x[i+1]-x[i]

    ans=0
    for i in range(n-1):
        if a*y[i]<=b:
            ans+=a*y[i]
        else:
            ans+=b

    print(ans)

if __name__=="__main__":
    main()