k, toayen, fromayen = map(int, input().split())
ans1 = k + 1
k -= (toayen - 1)
d, m = divmod(k, 2)
ans2 = (fromayen - toayen) * d + toayen + m
print(max(ans1, ans2))