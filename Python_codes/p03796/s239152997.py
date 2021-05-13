n = int(input())
mod = 10**9+7
total = 1
for i in range(1,n+1):
    total *= i
    total = total%mod

print(total)
