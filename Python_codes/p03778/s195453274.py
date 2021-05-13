w, a, b = map(int, input().split())

if a + w < b:
    ans = b - (a + w)
elif b + w >= a and a + w >= b:
    ans = 0
else:
    ans = a - (b + w)
print(int(ans))