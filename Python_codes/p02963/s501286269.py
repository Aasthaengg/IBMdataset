n = int(input())
mod = 10**9
print(0,0,mod,1,(mod-n%mod)%mod,(n+(mod-n%mod)%mod)//mod)