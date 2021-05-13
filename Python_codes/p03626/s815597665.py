import sys
readline=sys.stdin.readline

def main():
    p=10**9+7
    n=int(input())
    s1=readline().strip()
    s2=readline().strip()
    pl=[]
    tempiter=iter(range(n))
    for i in tempiter:
        if s1[i]==s2[i]:
            pl.append(0)
        else:
            pl.append(1)
            _=next(tempiter)
    ans=1
    #print(pl)
    for i,_ in enumerate(pl[:-1]):
        s=pl[i]-pl[i+1]+2*pl[i]*pl[i+1]
        if s==0:
            ans=ans*2 % p
        elif s==1:
            ans=ans*2 % p
        elif s==2:
            ans=ans*3 % p
    if pl[-1]==0:
        ans=ans*3 % p
    else:
        ans=ans*6 % p
    print(ans)

if __name__=='__main__':
    main()
