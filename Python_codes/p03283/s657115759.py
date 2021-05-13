n, m, q = map(int, input().split())

train = [[0 for _ in range(501)] for _ in range(501)]
train_total = [[0 for _ in range(501)] for _ in range(501)]
query = []

for i in range(m):
    a, b = map(int, input().split())
    train[a][b] += 1

for j in range(q):
    x, y = map(int, input().split())
    query.append([x, y])

for left in range(0, 501):
    cnt = 0
    for right in range(0, 501):
        cnt += train[left][right]
        train_total[left][right] = cnt

for left, right in query:
    total = 0
    for row in range(left, right+1):
        num2 = train_total[row][right]
        num1 = train_total[row][left-1]
        total += (num2 - num1)
    print(total)