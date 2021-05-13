n=int(input())
ma,r=0,0
for _ in range(n):
    a,b=map(int,input().split())
    if ma<a:
        ma=a
        r=ma+b
print(r)