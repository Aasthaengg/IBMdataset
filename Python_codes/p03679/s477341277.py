x, a, b = map(int, input().split())

if a - b >= 0:
    ans = "delicious"
elif a + x - b >= 0:
    ans = "safe"
else:
    ans ="dangerous"

print(ans)