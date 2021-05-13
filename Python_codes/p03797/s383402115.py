from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())

    ans=0
    t=min(n,m//2)
    ans+=t
    n-=t
    m-=2*t
    ans+=m//4
    print(ans)
    
if __name__=="__main__":
    main()