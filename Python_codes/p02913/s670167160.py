def main():
    import sys
    input=sys.stdin.buffer.readline
    n=int(input())
    b=129
    M=2**61-1
    x,y=1,0
    f=[x]*(n+2)
    h=[y]*(n+2)
    for i,c in enumerate(input()):
        f[i+1]=x=x*b%M
        h[i+1]=y=(y*b+c)%M
    ok,ng=0,n//2+1
    while ng-ok>1:
        mid=ok+ng>>1
        d={}
        for i in range(0,n-mid+1):
            k=(h[i+mid]-h[i]*f[mid])%M
            if k in d:
                if d[k]+mid<=i:
                    ok=mid
                    break
            else:
                d[k]=i
        else:
            ng=mid
    print(ok)
main()