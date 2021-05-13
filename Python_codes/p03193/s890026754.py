n, h, w = map(int, input().split())
res = 0
for _ in range(n):
    hh,ww = map(int, input().split())
    if hh >= h and ww >= w:
        res += 1
print(res)

