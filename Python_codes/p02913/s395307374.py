def main():
    import sys
    input=sys.stdin.buffer.readline
    n=int(input())
    b,M=37,998244353
    x,y=1,0
    f,h=[1],[0]
    f_add,h_add=f.append,h.append
    for c in input():
        x=x*b%M
        f_add(x)
        y=(y*b+c)%M
        h_add(y)
    ok,ng=0,n//2+1
    while ng-ok>1:
        mid=ok+ng>>1
        d={}
        for i in range(n-mid+1):
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