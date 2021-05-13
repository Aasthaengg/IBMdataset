n,m = map(int, input().split())

if abs(n-m) >1:
    print(0)
    exit()

p = 10**9+7
fact =[1,1]
for i in range(2, max(n,m) + 1):
    fact.append((fact[-1] * i) % p)
    
if n ==m:
    res = fact[n]*fact[m]*2

else:
    res = fact[n]*fact[m]

print(res%p)