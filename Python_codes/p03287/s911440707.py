def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))

    pmod={}
    cummod=0
    for num in a:
        cummod+=num
        cummod%=m
        if cummod not in pmod:
            pmod[cummod]=1
        else:
            pmod[cummod]+=1
    
    if 0 in pmod:
        ans=pmod[0]
    else:
        ans=0
        
    for i in pmod:
        if pmod[i] >=2 :
            ans+=pmod[i]*(pmod[i]-1)//2
    
    print(ans)

if __name__=='__main__':
    main()