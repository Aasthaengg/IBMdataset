x = int(input())

cnt = 2 * (x // 11)
cnt += (0 if x % 11 == 0 else 1 if x % 11 <= 6 else 2)

print(cnt)