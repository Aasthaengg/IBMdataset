n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

l = sorted([[a + b, a, b] for a, b in ab])[::-1]
res = 0
for idx, i in enumerate(l):
    if idx % 2 == 0:
        res += i[1]
    else:
        res -= i[2]
print(res)
