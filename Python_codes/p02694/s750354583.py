n = int(input())

cnt = 0
cur = 100
while n > cur:
    cur += cur // 100
    cnt += 1

print(cnt)
