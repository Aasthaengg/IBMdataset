from sys import stdin
def main():
    #入力
    readline=stdin.readline
    x=int(readline())

    l=0
    r=10**9
    while l<r-1:
        m=(l+r)//2
        if m*(m+1)//2>=x:
            r=m
        else:
            l=m

    print(r)

if __name__=="__main__":
    main()