n, a, b = map(int, input().split())

if(b < a):
    swap(a, b)

ans = -1
if a%2 == b%2:
    ans = (b - a) // 2

else:
    x = a + (b - a) // 2
    a = n - a + 1
    b = n - b + 1
    y = a + (b - a) // 2
    ans = min(x, y)

print(ans)
