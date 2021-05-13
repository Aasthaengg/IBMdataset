h, w, n = map(int, input().split())
d = dict()
ans = [0] * 10
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(-1, 2):
        for j in range(-1, 2):
            x, y = a + i, b + j
            if 1 < x < h and 1 < y < w:
                k = x * w + y
                if not k in d:
                    d[k] = 1
                    ans[1] += 1
                else:
                    ans[d[k]] -= 1
                    ans[d[k] + 1] += 1
                    d[k] += 1
ans[0] = (h - 2) * (w - 2) - sum(ans)
for i in ans:
    print(i)