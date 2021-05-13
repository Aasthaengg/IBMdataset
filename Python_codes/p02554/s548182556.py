N = int(input())
mod = 10 ** 9 + 7
alln = pow(10,N,mod)
zeronine = pow(9,N,mod)
nothing = pow(8,N,mod)
ans = (alln - zeronine * 2 + nothing) % mod
print(ans)