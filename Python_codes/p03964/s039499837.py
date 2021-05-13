n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]
pt, pa = 1, 1
for i in range(n):
    t, a = ta[i]
    v = max((pt + t - 1) // t, (pa + a - 1) // a)
    pt = v * t
    pa = v * a

print(pt + pa)