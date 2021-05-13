mod = 10**9+7

N = int(input())
a = 1
for n in range(N):
    a = a*(n+1)%mod
print(a)