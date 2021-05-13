from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    ans=0
    for i in range(n):
        ans+=a[i]-1

    print(ans)

if __name__=="__main__":
    main()