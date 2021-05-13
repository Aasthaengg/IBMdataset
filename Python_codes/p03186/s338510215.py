a,b,c = map(int,input().split())

ans = 0
if c <= a + b:
    ans = b + c
else:
    ans = b + a+b
    if c - (a+b) > 0:
        ans += 1

print(ans)