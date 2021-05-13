
a, b, c = map(int, input().split())
ans = 0

if a + b + 1 >= c:
    ans = c + b
else:
    ans = a + b + b + 1
print(ans)