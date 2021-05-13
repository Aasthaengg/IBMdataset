w, a, b = map(int, input().split())

if a > b:
    c = a
    a = b
    b = c

ans = b - (a+w)

if ans < 0:
    ans = 0

print(ans)