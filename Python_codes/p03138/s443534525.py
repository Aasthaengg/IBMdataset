import sys
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    
    bin_k=format(k,'b').zfill(50)
    l=50
    
    flag=False
    power=pow(2,l-1)
    ans=0
    for i in range(l):
        keta=l-i-1
        cnt=0
        for num in a:
            if (num>>keta)&1:
                cnt+=1

        if flag:
            ans+=max(cnt,n-cnt)*power
        
        else:
            if 2*cnt >= n and bin_k[i]=='1':
                flag=True
                ans+=cnt*power
          
            elif 2*cnt >= n:
                ans+=cnt*power
           
            elif bin_k[i]=='1':
                ans+=(n-cnt)*power
       
            else:
                ans+=cnt*power
        
        power//=2
    
    print(ans)
if __name__=='__main__':
    main()
