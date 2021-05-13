def main():
    n,p=map(int,input().split())
    s=list(map(int,list(input())))
    cnt,ans=0,0
    m=[0]*p
    m[0]=1

    if p in [2, 5]:
        for i, x in enumerate(s):
            if x % p == 0:
                ans += i + 1
        print(ans)
        exit()

    sm=0
    d=1
    for i in range(n):
        sm=(sm+s[n-1-i]*d)%p
        m[sm]+=1
        d=(d*10)%p
    
    for i in m:
        ans+=i*(i-1)//2

    print(ans)

if __name__ == '__main__':
    main()