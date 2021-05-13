def main():
    n=int(input())
    a=[int(input()) for _ in [0]*n]
    ans=a[n-1]
    if ans>n-1:
        print(-1)
        return 0
    for i in range(n-2,-1,-1):
        if a[i]>i:
            print(-1)
            return 0
        elif a[i]+1==a[i+1]:
            continue
        elif a[i]+1<a[i+1]:
            print(-1)
            return 0
        else:
            ans+=a[i]
    print(ans)
main()