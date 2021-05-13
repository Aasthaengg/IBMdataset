from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    s=[a[0]]*n
    for i in range(1,n):
        s[i]=s[i-1]+a[i]

    cnt1=0
    s1=s[:]
    f1=0
    #1,-1,...
    for i in range(n):
        if i%2==0:
            if s1[i]+f1<=0:
                cnt1+=abs(1-s1[i]-f1)
                f1+=1-s1[i]-f1
        else:
            if s1[i]+f1>=0:
                cnt1+=abs(-1-s1[i]-f1)
                f1+=-1-s1[i]-f1
    
    cnt2=0
    s2=s[:]
    f2=0
    #-1,1,...
    for i in range(n):
        if i%2==0:
            if s2[i]+f2>=0:
                cnt2+=abs(-1-s2[i]-f2)
                f2+=-1-s2[i]-f2
        else:
            if s2[i]+f2<=0:
                cnt2+=abs(1-s2[i]-f2)
                f2+=1-s2[i]-f2
    print(min(cnt1,cnt2))

if __name__=="__main__":
    main()