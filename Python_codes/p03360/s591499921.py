a,b,c=map(int,input().split())
d=int(input())
n=max(a,b,c)
for _ in range(d):
    n=n*2
print(n+a+b+c-max(a,b,c))