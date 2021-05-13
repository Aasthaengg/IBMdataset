a,b,c=map(int,input().split())
k=int(input())

m=max(a,b,c)
for _ in range(k):
    m*=2

print(a+b+c+m-max(a,b,c))