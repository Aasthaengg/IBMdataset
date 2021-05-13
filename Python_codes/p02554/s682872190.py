n = int(input())
mod = 10**9 + 7
x = pow(8,n,mod)
zero = pow(10,n,mod) - pow(9,n,mod)
nine = pow(10,n,mod) - pow(9,n,mod)
print((x+zero+nine-pow(10,n,mod))%mod)