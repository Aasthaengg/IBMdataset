n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))

def bin_a(list,bi):
    ok=-1
    ng=n
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if bi>list[mid]:
            ok=mid
        else:
            ng=mid
    return ok+1
def bin_c(list,bi):
    ok=n
    ng=-1
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if bi<list[mid]:
            ok=mid
        else:
            ng=mid
    return n-ok

cnt=0
for i in range(n):
    cnt+=bin_a(a,b[i])*bin_c(c,b[i])
    #print(bin_a(a,b[i]),bin_c(c,b[i]))
print(cnt)