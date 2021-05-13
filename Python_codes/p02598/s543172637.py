n,k=map(int, input().split())
A=[int(i) for i in input().split()]
ng=0
ok = max(A)
while(ng+1!=ok):
    mid = (ok+ng)//2
    ans = 0
    for i in A:
        ans += 0--i//mid-1
    if(ans<=k):
        ok = mid
    else:
        ng = mid
print(ok)
