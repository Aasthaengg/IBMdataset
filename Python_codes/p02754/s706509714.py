n, a, b = map(int, input().split())
ans = 0
ans = (n//(a+b)) * a
if n%(a+b) > a:
    ans += a
else:
    ans += n%(a+b)
print(ans)