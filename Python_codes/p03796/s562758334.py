N = int(input())
a=1
for i in range(1,N+1):
    a*=i
    a%=(10**9+7)
print(a%(10**9+7))