a, b, m = map(int, input().split())
a =list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(m)]

aMin = min(a)
bMin = min(b)
ans = aMin + bMin

for xycm in xyc:
    x = xycm[0] - 1
    y = xycm[1] - 1
    c = xycm[2]
    p = a[x] + b[y] - c

    if p < ans:
        ans = p

print(ans)