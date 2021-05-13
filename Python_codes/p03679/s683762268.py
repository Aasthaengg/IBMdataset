x, a, b = [int(s) for s in input().split()]
if b <= a:
    ans = "delicious"
elif b <= a + x:
    ans = "safe"
else:
    ans = "dangerous"
print(ans)