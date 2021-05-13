n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(key=lambda x:x[0])

num, cost = 0, 0
for a, b in AB:
    if num + b > m:
        b = m - num

    num += b
    cost += a * b

    if num == m:
        break

print(cost)