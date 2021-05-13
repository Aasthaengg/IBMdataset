x,y = map(int,input().split())

mod = 10**9 + 7

if (x+y)%3 != 0:
    print(0)
    
else:
    
    n=(x+y)//3
    
    r = min(x-n,y-n)
    
    if r<0:
        print(0)
        
    else:
    
        p=1
        q=1
        for i in range(r):
           
            p *= n-i
            p %= mod
            
    
            q *= i+1
            q %= mod
                
        ans = p * pow(q,mod-2,mod)
        ans %= mod
            
        print(ans)