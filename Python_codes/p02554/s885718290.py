n = int(input())
mod = 10**9 + 7

c = 10**n - (2*9**n - 8**n)
r = c % mod
print(r)