from sys import stdin
def check(n,s,x):
    cnt=0
    f=0
    for i in range(n):
        if i%2==0:
            if (s[i]+f)*x<=0:
                cnt+=abs(x-s[i]-f)
                f+=x-s[i]-f
        else:
            if (s[i]+f)*x>=0:
                cnt+=abs(-x-s[i]-f)
                f+=-x-s[i]-f
    return cnt

def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    s=[a[0]]*n
    for i in range(1,n):
        s[i]=s[i-1]+a[i]

    cnt1=check(n,s,1)
    cnt2=check(n,s,-1)
    print(min(cnt1,cnt2))

if __name__=="__main__":
    main()