n,m = map(int,input().split())

mod = 10**9 + 7

if abs(n-m) >= 2:
    print(0)
else:
    dog = 1
    mon = 1
    
    for i in range(n,0,-1):
        dog *= i
        dog %= mod
        
    for i in range(m,0,-1):
        mon *= i 
        mon %= mod
        
    if abs(n-m) == 0:
        print(dog*mon*2%mod)
    else:
        print(dog*mon%mod)