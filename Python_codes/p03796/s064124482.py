n=int(input())
res=1
for i in range(n):
    res*=(i+1)
    if res>=10**9+7:
        res%=(10**9+7)
print(res)
