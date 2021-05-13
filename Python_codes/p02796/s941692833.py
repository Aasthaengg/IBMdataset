N = int(input())
XL = []
for _ in range(N):
    x, l = map(int, input().split())
    XL.append([x - l, x + l])
XL.sort(key=lambda x: x[1])

res = 0
now = -10 ** 9
for s, e in XL:
    if now <= s:
        now = e
        res += 1

print(res)
