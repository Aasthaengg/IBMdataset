def main():
    s=input()
    k=int(input())
    if s.count(s[0])==len(s):
        print(len(s)*k//2)
    else:
        ans=0
        cnt=1
        res=[0,0]
        t=s+"X"
        flg=0
        for i in range(len(s)):
            if t[i]==t[i+1]:
                cnt+=1
            else:
                if flg==0:
                    res[0]=cnt
                    flg=1
                elif i==len(s)-1:
                    res[1]=cnt
                ans+=cnt//2
                cnt=1
        ans*=k
        if s[0]==s[-1] and res[0]%2==1 and res[1]%2==1:
            ans+=k-1
        print(ans)
if __name__=="__main__":
    main()