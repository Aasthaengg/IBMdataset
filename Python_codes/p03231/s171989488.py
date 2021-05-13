import fractions
def main():
    n,m=map(int,input().split())
    s=input()
    t=input()
    ans=-1
    gcd0=fractions.gcd(n,m)
    lcm=n*m//gcd0
    flg=1
    for i in range(gcd0):
        if s[n*i//gcd0]!=t[m*i//gcd0]:
            flg=0
            break
    if flg==1:
        ans=lcm
    print(ans)
if __name__=="__main__":
    main()