
X = int(input())

cnt = X // 11
X -= 11 * cnt

cnt *= 2
sum = 0
y = 5 if cnt % 2 == 1 else 6
while sum < X:
  sum += y
  y = 6 if y == 5 else 5
  cnt += 1

print(cnt)