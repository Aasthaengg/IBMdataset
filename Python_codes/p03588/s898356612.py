n=int(input())
a,b=10**9,10**9
for i in range(n):
    at,bt=map(int,input().split())
    if bt<=b:
        a,b=at,bt
print(a+b)
