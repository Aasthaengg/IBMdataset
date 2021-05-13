def resolve():
    n=int(input())
    lv=list(map(int, input().split()))
    lc=list(map(int, input().split()))
    ans=0
    for i in range(n):
        if lv[i]>lc[i]:
            ans+=lv[i]-lc[i]
    print(ans)
resolve()