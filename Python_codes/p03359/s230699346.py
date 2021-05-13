a, b = [int(i) for i in input().split()]

ans = 0
ans += a - 1
if b >= a:
    ans += 1
print(ans)
