n, x, t = map(int, input().split())
ans = t * (n//x)
print(ans+t if n%x else ans)