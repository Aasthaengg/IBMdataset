w, a, b = [int(x) for x in input().split()]
ans = 0
if a + w < b:
    ans = b - (a + w)
elif b + w < a:
    ans = a - (b + w)
print(ans)