def main():
    n=int(input())
    X=input().strip()
    cnt_1=X.count('1')
    k1,k2=int(X,2)%(cnt_1-1) if cnt_1!=1 else 0,int(X,2)%(cnt_1+1)
    for i,x in enumerate(X):
        ans=0
        if x=='0':
            k=k2+pow(2,n-i-1,cnt_1+1)
            k%=cnt_1+1
            ans+=1
            while k:
                num=bin(k).count('1')
                k%=num
                ans+=1
        elif x=='1' and cnt_1!=1:
            k=k1-pow(2,n-i-1,cnt_1-1)
            k%=cnt_1-1
            ans+=1
            while k:
                num=bin(k).count('1')
                k%=num
                ans+=1
        else:
            ans=0
        print(ans)
    
if __name__=='__main__':
    main()