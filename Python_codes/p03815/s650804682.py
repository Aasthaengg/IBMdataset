x = int(input())
ans = (x // 11) * 2
point = x % 11
if point != 0 and point <= 6: ans += 1
elif point != 0 : ans += 2
print(ans)
