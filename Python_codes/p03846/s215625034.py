n=int(input())
a=list(map(int,input().split()))
mod=10**9+7

a.sort()

if n%2==0:
    for i in range(n//2):
        if a[i*2]!=i*2+1 or a[i*2+1]!=i*2+1:
            print(0)
            exit()
    
    print((2**(n//2))%mod)


else:
    if a[0]!=0:
        print(0)
        exit()
    
    b=a[1:]

    for i in range(n//2):
        if b[i*2]!=i*2+2:
            print(0)
            exit()
        
        if b[i*2+1]!=i*2+2:
            print(0)
            exit()

    print((2**(n//2))%mod)