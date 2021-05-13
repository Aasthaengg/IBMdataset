a, b, c = map(int, input().split())
cnt = 0
while True:
    if a % 2 or b % 2 or c % 2:
        break
    if a == b == c:
        cnt = -1
        break
    a, b, c = b // 2 + c // 2, c // 2 + a // 2, a // 2 + b // 2
    cnt += 1
print(cnt)