a, b = (int(i) for i in input().split())
ans = a
if a > b: ans -= 1
print(ans)