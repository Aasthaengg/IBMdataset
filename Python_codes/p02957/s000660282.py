a, b = map(int, input().split())
ans = abs(a - b) / 2
if ans.is_integer():
    ans = max(a, b) - int(ans)
    print(ans)
else:
    print("IMPOSSIBLE")
