A, B = map(int, input().split())

ans = 0
for i in range(A, B + 1):
    a = str(i)
    b = ''
    for j in range(1, len(a) + 1):
        b += a[-j]
    if a == b:
        ans += 1
print(ans)
