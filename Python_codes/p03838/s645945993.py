x, y = map(int, input().split())
ans = 0
x2 = -x
y2 = -y
L = [y - x, y - x2, y2 - x, y2 - x2]
Labs = [abs(y - x), abs(y - x2), abs(y2 - x), abs(y2 - x2)]
ans += min(Labs)
i = L.index(min(Labs))
if i == 1 or i == 2:
    ans += 1
elif i == 3:
    ans += 2
print(ans)
