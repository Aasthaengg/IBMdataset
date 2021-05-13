n=int(input())
a=1
for i in range(1,n+1):
    a*=i
    if a>10**9+7:
        a=a%(10**9+7)
print(a)