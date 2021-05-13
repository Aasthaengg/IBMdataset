n, c, *t = map(int, open(0).read().split())
right = [0]
left = [0]
sushi = tuple([(0, 0)]) + tuple(zip(t[::2], t[1::2])) + tuple([(c, 0)])
for i in range(1, n + 1):
    x, v = sushi[i]
    y = sushi[i - 1][0]
    cost = right[-1] + v - (x - y)
    right.append(cost)
    x, v = sushi[n + 1 - i]
    y = sushi[n + 2 - i][0]
    cost = left[-1] + v - (y - x)
    left.append(cost)
ans = max(right + left)
right_max = right[:]
left_max = left[:]
for i in range(1, n + 1):
    right_max[i] = max(right_max[i], right_max[i - 1])
    left_max[i] = max(left_max[i], left_max[i - 1])
for i in range(1, n + 1):
    ans = max(ans, \
            right[i] - sushi[i][0] + left_max[n - i], \
            left[i] - c + sushi[n + 1 - i][0] + right_max[n - i])
print(ans)