from sys import stdin

def nC2(n):
    return n*(n-1)//2

def main():
    #入力
    readline=stdin.readline
    s=readline().strip()

    d=dict()
    p=1
    t=0
    for i in range(len(s)-1,-1,-1):
        n=int(s[i])
        m=(n*p+t)%2019
        t=m
        p*=10
        p%=2019
        if m not in d:
            d[m]=1
        else:
            d[m]+=1
        
    if 0 in d:
        ans=d[0]
    else:
        ans=0
    for v in d.values():
        ans+=nC2(v)
    print(ans)
    
if __name__=="__main__":
    main()