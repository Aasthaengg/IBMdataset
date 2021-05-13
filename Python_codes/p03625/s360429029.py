from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    a.sort()
    ans1,ans2=0,0
    j=-1
    for i in range(n-1,-1,-1):
        if i==n-1:
            m=a[i]
        else:
            if a[i]!=m:
                m=a[i]
            else:
                ans1=m
                j=i
                break

    for i in range(j-1,-1,-1):
        if i==j-1:
            m=a[i]
        else:
            if a[i]!=m:
                m=a[i]
            else:
                ans2=m
                break

    print(ans1*ans2)

if __name__=="__main__":
    main()