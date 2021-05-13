N=int(input())
mod = 10**9+7
A=10**N%mod-2*9**N%mod+8**N%mod
print(A%mod)