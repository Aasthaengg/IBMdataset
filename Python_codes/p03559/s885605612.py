import sys
input=sys.stdin.readline
n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))

ans=0
def ab_check(list_count,i):
    ok=-1
    ng=n
    B=b[i]
    while ng-ok>1:
        mid=(ok+ng)//2
        if list_count[mid]<B:
            ok=mid
        else:
            ng=mid
    #print(ok+1,'A')
    return ok+1

def bc_check(list_count,i):
    ok=n
    ng=-1
    B=b[i]
    while ok-ng>1:
        mid=(ok+ng)//2
        if list_count[mid]>B:
            ok=mid
        else:
            ng=mid
    #print(n-ok,'B')
    return n-ok
    #print(i,ok)

for i in range(n):
    ans+=ab_check(a,i)*bc_check(c,i)
print(ans)
#print(a,c,sep='\n')