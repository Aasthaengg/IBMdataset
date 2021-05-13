a,b,c = map(int, input().split())
ans = 0
if a + b > c:
    ans = c + b
elif a + b == c:
    ans = c + b
else:
    ans = a + (b * 2) + 1
print(ans)