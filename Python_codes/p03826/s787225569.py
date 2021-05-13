a,b,c,d = map(int, input().split())
ans = a*b
if c*d > ans:
    ans = c*d

print(ans)