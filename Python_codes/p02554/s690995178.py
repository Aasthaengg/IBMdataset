N = int(input())
mod = 1000000000 + 7
ans = pow(10,N,mod)
ans -= 2 * pow(9,N,mod)
ans += pow(8,N,mod)
print(ans%mod)