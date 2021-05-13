X, Y = map(int, input().split())
x = X
ans = 1
while x * 2 <= Y:
    x *= 2
    ans += 1
print(ans)