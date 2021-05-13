x=int(input())

ans=0

for b in range(1, int(x**(1/2)+1)):
    for p in range(2, 20):
        c = b**p
        if c<=x:
            ans=max(ans, c)

print(ans)