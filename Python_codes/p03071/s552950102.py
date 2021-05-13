a,b = map(int, input().split())
ans = 0
ans += max(a,b)
ans += max(max(a,b)-1, min(a,b))
print(ans)