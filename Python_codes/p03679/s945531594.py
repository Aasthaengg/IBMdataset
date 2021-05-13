x, a, b = map(int, input().split())

if b <= a:
    ans = "delicious"
elif b > a and b <= a + x:
    ans = "safe"
else:
    ans = "dangerous"
print(ans)