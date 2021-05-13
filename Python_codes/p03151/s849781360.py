def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    minus=0
    ans=0
    if sum(a)<sum(b):
        print(-1)
    else:
        for i in range(n):
            dif=a[i]-b[i]
            if dif>0:
                c.append(dif)
            elif dif<0:
                ans+=1
                minus+=dif
        c.sort(reverse=True)
        i=0
        while minus<0:
            minus+=c[i]
            i+=1
        print(ans+i)
if __name__=="__main__":
    main()