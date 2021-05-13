def main():
    from collections import Counter
    n=int(input())
    a=Counter(map(int,input().split()))
    mod=10**9+7

    if n%2==1:
        if 0 not in a:
            print(0)
            exit()
        else:
            if a[0]!=1:
                print(0)
                exit()
            else:
                a[0]=2
    
    for k,v in a.items():
        if v!=2 or (n-k-1)%2==1:
            print(0)
            exit()
            
    print(2**(n//2)%mod)  
if __name__=='__main__':
    main()