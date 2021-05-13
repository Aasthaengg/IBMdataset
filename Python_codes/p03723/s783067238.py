a, b, c = map(int, input().split())

cnt = 0

while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        break
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and a == b and b == c and c == a:
        cnt = -1
        break

    a, b, c = (b + c) / 2, (a + c) / 2, (a + b) / 2
    cnt += 1

print(cnt)
