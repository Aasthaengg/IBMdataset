a,b,c = map(int,input().split())
ans = 0

if a == b:
    ans = c
else:
    if a == c:
        ans = b
    else:
        ans = a

print(ans)