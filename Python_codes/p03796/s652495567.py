p=1
N =int(input())
for i in range(1,N+1):
    p = p * i
    p %= (10**9+7)
print(p)