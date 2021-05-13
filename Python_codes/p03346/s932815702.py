def main():
    import bisect
    n=int(input())
    a=[int(input()) for _ in [0]*n]
    b=[[a[i],i] for i in range(n)]
    b.sort()
    cnt=1
    ans=1
    for i in range(1,n):
        if b[i-1][1]<b[i][1]:
            cnt+=1
            ans=max(cnt,ans)
        else:
            cnt=1
    print(n-ans)
main()