n, K = map(int, input().split())
point = []
x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))
    x_list.append(x)
    y_list.append(y)
x_list.sort()
y_list.sort()

ans = 4 * (10 ** 18)
for i in range(len(x_list)):
    for j in range(i + 1, len(x_list)):
        for k in range(len(y_list)):
            for l in range(k + 1, len(y_list)):
                num = 0
                for x, y in point:
                    if (x_list[i] <= x <= x_list[j]) & (y_list[k] <= y <= y_list[l]):
                        num += 1
                if num >= K:
                    ans = min(ans, abs((x_list[j] - x_list[i]) * (y_list[l] - y_list[k])))
print(ans)