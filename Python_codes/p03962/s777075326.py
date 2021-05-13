a,b,c = map(int,input().split())
ans = 3
if a == b:
    ans = 2
if a == c:
    ans = 2
if b == c:
    ans = 2
if a == b == c:
    ans = 1

print(ans)