a, b, c = map(int, input().split())
ans = b//a
print(ans if c>ans else c)