from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    m=n//2
    a=list(map(int,readline().split()))

    s=sum(a)//2
    ans=[0]*n
    k=n-1
    t=0
    if n==3:
        for i in range(n):
            ans[k]=(s-a[i])*2
            k+=1
            k%=n
    else:
        for i in range(n):
            if i==0:
                tmp=i
                for j in range(m):
                    t+=a[i]
                    i+=2
                    i%=n
                nex=i
            else:
                t-=a[tmp]
                tmp+=2
                tmp%=n
                t+=a[nex]
                nex+=2
                nex%=n
            ans[k]=(s-t)*2
            k+=2
            k%=n

    print(*ans)

if __name__=="__main__":
    main()