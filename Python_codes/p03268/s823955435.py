n,k = map(int,input().split())
ans = 0
if k%2 == 0:
    #k mod halfの個数は
    mod1 = (n+(k//2))//k
    #k mod0の個数は
    mod2 = n//k
    
    ans += mod1**3 + mod2**3
    
else:
    #kmod0の個数は
    modk = n//k
    
    ans += modk**3
print(ans)