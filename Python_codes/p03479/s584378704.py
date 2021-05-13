X, Y = map(int, input().split())
ans = 1
while X <= Y:
    X *= 2
    if X > Y:
        break
    ans += 1

print(ans)