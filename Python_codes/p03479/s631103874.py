x, y = map(int, input().split())
ans = 0
check = x
while check <= y:
    ans += 1
    check = x*(2**ans)
print(ans)
