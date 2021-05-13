a,b,c = map(int,input().split())
k = int(input())

m = max(a,b,c)

for i in range(k):
    m *= 2

ans = a+b+c+m-max(a,b,c)

print(ans)