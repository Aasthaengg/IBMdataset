x, y = map(int, input().split())
ans = min(abs(x+y)+1, max(y-x, x-y+2))
print(ans)