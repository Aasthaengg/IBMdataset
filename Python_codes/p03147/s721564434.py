n =int(input())
h=list(map(int,input().split()))
ans=0
p=0
for i in range(n):
    if h[i]>=p:
        ans+=h[i]-p
    p=h[i]

print(ans)