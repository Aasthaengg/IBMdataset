n = int(input())
a,b=map(int,input().split())
for i in range(n-1):
    c,d=map(int,input().split())
    a=max(a,c)
    if a==c:
        b=d
print(a+b)