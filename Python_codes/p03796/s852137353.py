n = int(input())
p = 1
MOD = 10**9+7
for i in range(n): p = p*(i+1)%MOD
print(p)