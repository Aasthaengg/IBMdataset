def main():
    n,k=map(int,input().split())
    v=list(map(int,input().split()))
    ans=0
    for a in range(min(n,k)+1):
        for b in range(min(n,k)-a+1):
            chk=v[:a]+v[n-b:]
            chk.sort()
            x,s=0,sum(chk)
            while x<k-(a+b) and len(chk)>x:
                s-=min(0,chk[x])
                x+=1
            ans=max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()
