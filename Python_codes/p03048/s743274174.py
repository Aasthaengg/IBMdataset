r,g,b,n=map(int,input().split())
ans = 0
for x in range(n+1):
    for y in range(n+1):
        if (n-(r*x)-(g*y))%b == 0 and (n-(r*x)-(g*y))>=0:
            ans += 1
print(ans)