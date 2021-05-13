a, b, c, k = map(int, input().split())
l = {1: a, 0: b, -1: c}
ans = 0
for i, j in l.items():
    if k >= j:
        ans += j * i
        k -= j
    else:
        ans += k * i
        break
print(ans)
