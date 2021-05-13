n=int(input())
if n%2==1:
    print(0)
    exit(0)

k=n//2

from math import floor

ans=0
deno=5
while deno<=k:
    ans+=k//deno
    deno*=5

print(ans)
