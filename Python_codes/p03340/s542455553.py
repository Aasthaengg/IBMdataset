from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    l=0
    r=1
    ans=0
    now_xor=a[0]
    now_sum=a[0]
    while l<n:
        if r<n:
            now_xor^=a[r]
            now_sum+=a[r]
            while now_xor!=now_sum:
                ans+=1
                ans+=r-l-1
                now_xor^=a[l]
                now_sum-=a[l]
                l+=1
            r+=1
        else:
            l+=1
            ans+=1
            ans+=r-l

    print(ans)

if __name__=="__main__":
    main()